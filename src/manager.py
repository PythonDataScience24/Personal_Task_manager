"""This module provides a class to manage tasks."""
import os
import json
from datetime import datetime, timedelta
import pandas as pd
from taskValidator import taskValidator

class Manager:
    """Class to manage tasks."""

    def __init__(self):
        """Initialize Manager class."""
        self.file_path = "tasklist.csv"
        self.create_tasklist()

    def create_tasklist(self):
         """Create a tasklist."""
         self.tasklist = pd.DataFrame(columns=[
             "Title", "Description", "Deadline", "Category",
             "Priority", "Status", "Completion Time",
             "Duration Planned", "Duration", "Points"
         ])
         if os.path.exists(self.file_path):
             self.tasklist = pd.read_csv(self.file_path)
             print("File found and loaded into a dataframe.")
         else:
             self.tasklist.to_csv(self.file_path, index=False)
             print("File not found. Created a new empty dataframe.")



    def add_task(self, title='', description="", deadline='',
                category=None, priority=0, status="To Do",
                completion_time=None, duration_planned=None,
                duration=None, points=0):
        """Add a task to the tasklist."""

        if not isinstance(self.tasklist, pd.DataFrame):
            # Create an empty tasklist if it's not already initialized
            self.create_tasklist()

        self.tasklist.loc[len(self.tasklist)] = [
            title, description,
            taskValidator.validateDeadline(deadline), category,
            taskValidator.validatePriority(priority),
            taskValidator.validateStatus(status),
            completion_time, duration_planned, 
            duration, points
        ]
        self.tasklist.to_csv(self.file_path, index=False)
        if status == 'In Progress':
            self.set_inprogress(len(self.tasklist)-1)


    def edit_task(self, i: int, title=None, description=None, deadline=None,
                  category=None, priority=None, status=None,
                  completion_time=None, duration_planned=None,
                  duration=None, points=None):
        """Edit a task in the tasklist."""
        if 0 <= i < len(self.tasklist):
            if title:
                self.tasklist.loc[i, "Title"] = title
            if description:
                self.tasklist.loc[i, "Description"] = description
            if deadline:
                self.tasklist.loc[i, "Deadline"] = taskValidator.validateDeadline(deadline)
            if category:
                self.tasklist.loc[i, "Category"] = category
            if priority:
                self.tasklist.loc[i, "Priority"] = taskValidator.validatePriority(priority)
            if status:
                self.tasklist.loc[i, "Status"] = taskValidator.validateStatus(status)
                if status == 'In Progress':
                    self.set_inprogress(i)
                if status == 'Completed':
                    self.complete_task(i)
            if completion_time:
                self.tasklist.loc[i, "Completion Time"] = taskValidator.validateDeadline(completion_time)
            if duration_planned:
                self.tasklist.loc[i, "Duration Planned"] = duration_planned
            if duration:
                self.tasklist.loc[i, "Duration"] = duration
            if points:
                self.tasklist.loc[i, "Points"] = points
            self.tasklist.to_csv(self.file_path, index=False)
        else:
            print("Index out of range.")

    def delete_task(self, i: int):
        """Delete a task from the tasklist."""
        if 0 <= i < len(self.tasklist):
            self.tasklist.drop(i, inplace=True)
            self.tasklist = self.tasklist.reset_index(drop=True)
            self.tasklist.to_csv(self.file_path, index=False)
        else:
            print("Index out of range.")

    def print_tasklist(self):
        """Print the tasklist."""
        print(self.tasklist)

    def set_inprogress(self, i):
        """Set a task to 'In Progress'."""
        if 0 <= i < len(self.tasklist):
            now = datetime.now()
            formatted_time = now.strftime(
                "%Y-%m-%d %H:%M"
                )
            filename = 'timestamps.json'
            data = []

            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    try:
                        data = json.load(file)
                        print("json file loaded")
                    except json.JSONDecodeError:
                        data = []

            data.append({
                "id": i,
                "time": formatted_time
            })

            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

            return 0

    def complete_task(self, i: int):
        """Complete a task."""
        if 0 <= i < len(self.tasklist):
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M")

            if not os.path.exists('timestamps.json'):
                print(f"No timestamps")
                return None

            with open('timestamps.json', 'r') as file:
                data = json.load(file)
                timestamp_str = next((entry['time'] for entry in data if entry['id'] == i), None)

            priority = self.tasklist.iloc[i]['Priority']
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
            duration = now - timestamp

            points = (duration.total_seconds() // 60) * priority

            self.edit_task(i, duration=duration.total_seconds()//60)
            self.edit_task(i, completion_time=formatted_time)
            self.edit_task(i, points=points)

        else:
            print("Index out of range.")

    def order_by(self, attribute, asc=True):
        """Sort the tasklist by a given attribute."""
        sort_functions = {
            'Title': lambda x: x.str.lower() + x,
            'Deadline': None,
            'Category': lambda x: x.str.lower(),
            'Priority': None,
            'Status': None,
            'Duration Planned': None,
            'i': None,
            'Points': None
        }

        if attribute in sort_functions:
            sorted_df = self.tasklist.sort_values(
                by=attribute, ascending=asc, key=sort_functions[attribute]
            )
            return sorted_df
        else:
            print(f"Invalid attribute: {attribute}")
            return None

    def add_category(self, new_category):
        """Add a new category to the tasklist."""
        categories = self.tasklist["Category"].unique()
        if new_category not in categories:
            self.tasklist["Category"].append(new_category)
            print(f"Category '{new_category}' added successfully.")
        else:
            print(f"Category '{new_category}' already exists.")

    def filter(self, **kwargs):
        """Filter the tasklist based on given criteria."""
        filtered_tasklist = self.tasklist.copy()

        # Convert priority to integer for comparison
        if 'Priority' in kwargs:
            kwargs['Priority'] = int(kwargs['Priority'])

        # Try to filter with all criteria first
        for attribute, value in kwargs.items():
            if attribute in self.tasklist.columns:
                filtered_tasklist = filtered_tasklist[filtered_tasklist[attribute] == value]
            else:
                print(f"Invalid attribute: {attribute}")

        return filtered_tasklist
    
    def get_tasklist(self):
        return self.tasklist

    def upcoming_deadlines(self):
        """Get upcoming deadlines."""
        tomorrow = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        return self.tasklist[self.tasklist['Deadline'] <= tomorrow]
    
