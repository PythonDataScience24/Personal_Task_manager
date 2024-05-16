import json
import os
import pandas as pd

class Profile:
    """
    A class to represent a profile.

    Attributes:
        name (str): The name of the profile.
        total_points (int): The total points earned by the profile.
        completed_tasks (int): The number of completed tasks.
        todo_tasks (int): The number of tasks to be done.
        inprogress_tasks (int): The number of tasks in progress.
        tasklist (DataFrame): DataFrame containing task information.
    """

    def __init__(self, name='None', total_points=0):
        """
        Initialize a profile with a name and total points.

        Args:
            name (str): The name of the profile. Defaults to 'None'.
            total_points (int): The total points of the profile. Defaults to 0.
        """
        self.name = name
        self.total_points = total_points
        self.completed_tasks = 0
        self.todo_tasks = 0
        self.inprogress_tasks = 0
        self.tasklist = pd.read_csv('tasklist.csv')
        self.tasklist['Deadline'] = pd.to_datetime(self.tasklist['Deadline'])
        self.calculate_completed_tasks()
        self.calculate_todo_tasks()
        self.calculate_inprogress_tasks()
        self.calculate_total_points()

    def calculate_completed_tasks(self):
        """
        Calculate the number of completed tasks.
        """
        completed_tasks = self.tasklist[self.tasklist['Status'] == 'Completed']
        self.completed_tasks = len(completed_tasks)

    def calculate_todo_tasks(self):
        """
        Calculate the number of tasks to do.
        """
        todo_tasks = self.tasklist[self.tasklist['Status'] == 'To Do']
        self.todo_tasks = len(todo_tasks)

    def calculate_inprogress_tasks(self):
        """
        Calculate the number of tasks in progress.
        """
        inprogress_tasks = self.tasklist[self.tasklist['Status'] == 'In Progress']
        self.inprogress_tasks = len(inprogress_tasks)

    def calculate_total_points(self):
        """
        Calculate the total points.
        """
        self.total_points = int(self.tasklist['Points'].sum())

    def to_dict(self):
        """
        Convert profile to dictionary.

        Returns:
            dict: Dictionary representation of the profile.
        """
        return {
            'name': self.name,
            'total_points': self.total_points,
            'completed_tasks': self.completed_tasks,
            'todo_tasks': self.todo_tasks,
            'ongoing_tasks': self.inprogress_tasks
        }
    
    def save_to_json(self, filename='profile.json'):
        """
        Save profile to JSON file.
        
        Args:
            filename (str): The filename to save the JSON data to. Defaults to 'profile.json'.
        """
        profile_dict = self.to_dict()
        data = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                try:
                    data = json.load(file)
                    index = next((index for (index, d) in enumerate(data) if d["name"] == self.name), None)
                    if index is not None:
                        data[index] = profile_dict
                    else:
                        data.append(profile_dict)
                except json.JSONDecodeError:
                    data.append(profile_dict)
        else:
            data.append(profile_dict)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def update_and_save(self, name=None, total_points=None):
        """
        Update profile attributes and save to JSON file.

        Args:
            name (str): The new name of the profile.
            total_points (int): The new total points of the profile.
        """
        if name is not None:
            self.name = name
        if total_points is not None:
            self.total_points = total_points
        self.calculate_completed_tasks()
        self.calculate_todo_tasks()
        self.calculate_inprogress_tasks()
        self.calculate_total_points()
        self.save_to_json()

    def __str__(self):
        """
        Return string representation of the profile.

        Returns:
            str: String representation of the profile.
        """
        return f"Name: {self.name}\nTotal Points: {self.total_points}\nCompleted Tasks: {self.completed_tasks}\nTodo Tasks: {self.todo_tasks}\nIn Progress Tasks: {self.inprogress_tasks}"

Profile().save_to_json()
