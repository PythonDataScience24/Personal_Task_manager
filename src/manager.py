import pandas as pd
import os
from  taskValidator import taskValidator
from datetime import datetime
import json






class Manager:
    def __init__(self):
        self.file_path = "tasklist.csv"
        self.create_tasklist()

    def create_tasklist(self):
        
        if os.path.exists(self.file_path):
            # Read the CSV into a DataFrame
            self.tasklist = pd.read_csv(self.file_path)
            print("File found and loaded into a dataframe.")
        else:
            # Create an empty DataFrame if the file does not exist
            self.tasklist = pd.DataFrame(columns=["Title", "Description", "Deadline", "Category", "Priority", "Status", "Completion Time", "Duration Planned", "Duration", "Points"])
            self.tasklist.to_csv(self.file_path, index=False)
            print("File not found. Created a new empty dataframe.")

    def add_task(self, title='', description="", deadline='', category=None, priority=0, status="To Do", completion_time=None, duration_planned=None, duration=None, points=None):
        if status == 'Completed':
            raise ValueError("Cannot add a task with status already 'Completed'.")
        
        self.tasklist.loc[len(self.tasklist)] = [title, description, taskValidator.validateDeadline(deadline), category, taskValidator.validatePriority(priority), taskValidator.validateStatus(status), completion_time, duration_planned, duration, points]
        self.tasklist.to_csv(self.file_path, index=False)
        #check it status in 'In Progress' and call the set_inprogress function
        if status == 'In Progress':
            self.set_inprogress(len(self.tasklist)-1)
        

    def edit_task(self, i: int, title=None, description=None, deadline=None, category=None, priority=None, status=None, completion_time=None, duration_planned=None, duration=None, points=None):
        if i < len(self.tasklist) and i >= 0:
            if title:
                #needs no restriction
                self.tasklist.at[i, "Title"] = title
            if description:
                #needs no restriction
                self.tasklist.at[i, "Description"] = description
            if deadline:
                #needs restriction, cant be in the past
                self.tasklist.at[i, "Deadline"] = taskValidator.validateDeadline(deadline)
            if category:
                # categories will get saved in a list ["Work", "Personal", "Health", "Other"] for example
                self.tasklist.at[i, "Category"] = category
            if priority:
                #either 0, 1, 2, 3
                self.tasklist.at[i, "Priority"] = taskValidator.validatePriority(priority)
            if status:
                #either "To Do", "In Progress", "Completed"
                self.tasklist.at[i, "Status"] = taskValidator.validateStatus(status)
                #if status is 'In Progress' call set_inprogress, if status is 'Completed' call complete_task
                if status == 'In Progress':
                    self.set_inprogress(i)
                if status == 'Completed':
                    self.complete_task(i)
            if completion_time:
                self.tasklist.at[i, "Completion Time"] = taskValidator.validateDeadline(completion_time)
            if duration_planned:
                self.tasklist.at[i, "Duration Planned"] = duration_planned
            if duration:
                self.tasklist.at[i, "Duration"] = duration
            if points:
                self.tasklist.at[i, "Points"] = points
            self.tasklist.to_csv(self.file_path, index=False)
        else:
            print("Index out of range.")

    def delete_task(self, i: int):
        if i < len(self.tasklist) and i >= 0:
            self.tasklist.drop(i, inplace=True)
            #self.order_by('i') #to make sure the original index is not changed (index shows recency)
            #maybe a way to restore the order before delet was called
            self.tasklist.reset_index(drop=True, inplace=True)
            self.tasklist.to_csv(self.file_path, index=False)
        else:
            print("Index out of range.")

    def print_tasklist(self):
        print(self.tasklist)

    def set_inprogress(self, i):
        if i < len(self.tasklist) and i >= 0:
            #saving current time in json
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M")
            filename = 'timestamps.json'
            data =[]

            #check if json file exists and open it
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    try:
                        data = json.load(file)
                        print("json file loaded")
                    except json.JSONDecodeError:
                        data = []
            
                    
                    
            #store the timestamp with id of the task
            data.append({
                "id"   : i,
                "time" : formatted_time
            })

            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

            return 0

    #not tested!!
    def complete_task(self, i: int):
        if i < len(self.tasklist) and i >= 0:
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M")
            
            #checks if file got created
            if not os.path.exists('timestamps.json'):
                print(f"No timestamps")
                return None
            
            #filters for correct timestamp
            with open('timestamps.json', 'r') as file:
                data = json.load(file)
                timestamp_str = next((entry['time'] for entry in data if entry['id'] == i), None)
            
            #extract priority for points calculation
            priority = self.tasklist.iloc[i]['Priority']
            #convert timestamp to a datetimeobject so we can substract it from now
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
            #creates a timedelta object which can be converted into seconds
            duration = now - timestamp
            #calc points (per min in this example)
            points = (duration.total_seconds() //60) * priority

            #edit
            self.edit_task(i, duration= duration.total_seconds()//60)
            self.edit_task(i, completion_time= formatted_time)
            self.edit_task(i, points= points)
            #add points (duration*Priority)
        
        else:
            print("Index out of range.")



    def order_by(self, attribute, asc=True):
        if attribute == 'Title':
            sortedbyTitle_df = self.tasklist.sort_values(by='Title', ascending=asc, key=lambda x: x.str.lower() + x)
            return sortedbyTitle_df
        
        if attribute == 'Deadline':
            sortedbyDeadline_df = self.tasklist.sort_values(by='Deadline', ascending=asc)
            return sortedbyDeadline_df
        
        if attribute == 'Category':
            sortedbyCategory_df = self.tasklist.sort_values(by='Category', ascending=asc, key=lambda x: x.str.lower())
            return sortedbyCategory_df

        if attribute == 'Priority':
            sortedbyPriority_df = self.tasklist.sort_values(by='Priority', ascending=asc) 
            return sortedbyPriority_df
        
        if attribute == 'Status':
            sortedbyStatus_df = self.tasklist.sort_values(by='Status', ascending=asc) #Completed last 
            return sortedbyStatus_df

        if attribute == 'Duration Planned':
            sortedbyDurationPlanned_df = self.tasklist.sort_values(by= 'Duration Planned', ascending=asc)
            return sortedbyDurationPlanned_df
        
        if attribute == 'i':
            sortedbyIndex_df = self.tasklist.sort_index(ascending=asc)
            return sortedbyIndex_df
        #currently only attributes which are predefined have an order_by function (missing Duration)
        if attribute == 'Points':
            sortedbyPoints_df = self.tasklist.sort_values('Points', ascending=asc)
            return sortedbyPoints_df
        
    def addCategory(self, newCategory):
        categories = self.tasklist["Category"].unique()
        if newCategory not in categories:
            self.tasklist["Category"].append(newCategory)
            print(f"Category '{newCategory}' added successfully.")
        else:
            print(f"Category '{newCategory}' already exists.")
            

    def filter(self, **kwargs):
        filtered_tasklist = self.tasklist.copy()
        for attribute, value in kwargs.items():
            if attribute in self.tasklist.columns:
                filtered_tasklist = filtered_tasklist[filtered_tasklist[attribute] == value]
            else:
                print(f"Invalid attribute: {attribute}")
        return filtered_tasklist
    
    def get_tasklist(self):
        return self.tasklist

