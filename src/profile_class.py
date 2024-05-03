import pandas as pd
import csv
import json
import os

class Profile:
    def __init__(self, name='None', total_points=0):
        self.name = name
        self.total_points = total_points
        # self.missed_deadlines = missed_deadlines
        self.completed_tasks = 0
        self.todo_tasks = 0
        self.ongoing_tasks = 0
        self.tasklist = pd.read_csv('tasklist.csv')
        self.tasklist['Deadline'] = pd.to_datetime(self.tasklist['Deadline'])
        self.calculate_completed_tasks()
        self.calculate_todo_tasks()
        self.calculate_inprogress_tasks()
        self.calculate_total_points()
        # self.calculate_missed_deadlines()

    def calculate_completed_tasks(self):
        completed_tasks = self.tasklist[self.tasklist['Status'] == 'Completed']
        self.completed_tasks = len(completed_tasks)
    
    def calculate_todo_tasks(self):
        todo_tasks = self.tasklist[self.tasklist['Status'] == 'To Do']
        self.todo_tasks = len(todo_tasks)
    
    def calculate_inprogress_tasks(self):
        inprogress_tasks = self.tasklist[self.tasklist['Status'] == 'In Progress']
        self.inprogress_tasks = len(inprogress_tasks)
    
    def calculate_total_points(self):
        self.total_points = int(self.tasklist['Points'].sum())

    # def calculate_missed_deadlines(self):
    #     missed_deadlines = self.tasklist[(self.tasklist['Status'] == 'In Progress') & (self.tasklist['Deadline'] < pd.Timestamp.now())]
    #     self.missed_deadlines = len(missed_deadlines)
    
    def to_dict(self):
        return {
            'name': self.name,
            'total_points': self.total_points,
            # 'missed_deadlines': self.missed_deadlines,
            'completed_tasks': self.completed_tasks,
            'todo_tasks': self.todo_tasks,
            'ongoing_tasks': self.inprogress_tasks
        }
    
    def save_to_json(self, filename='profile.json'):
        profile_dict = self.to_dict()
        data = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                try:
                    data = json.load(file)
                    # Find the index of the profile with the same name
                    index = next((index for (index, d) in enumerate(data) if d["name"] == self.name), None)
                    if index is not None:
                        # If a profile with the same name exists, update it
                        data[index] = profile_dict
                    else:
                        # If no profile with the same name exists, append a new one
                        data.append(profile_dict)
                except json.JSONDecodeError:
                    data.append(profile_dict)
        else:
            data.append(profile_dict)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def update_and_save(self, name=None, total_points=None):
        if name is not None:
            self.name = name
        if total_points is not None:
            self.total_points = total_points
        # if missed_deadlines is not None:
        #     self.missed_deadlines = missed_deadlines
        self.calculate_completed_tasks()
        self.calculate_todo_tasks()
        self.calculate_inprogress_tasks()
        self.calculate_total_points()
        # self.calculate_missed_deadlines()
        self.save_to_json()

    def __str__(self):
        return f"Name: {self.name}\nTotal Points: {self.total_points}\nCompleted Tasks: {self.completed_tasks}\nTodo Tasks: {self.todo_tasks}\nIn Progress Tasks: {self.inprogress_tasks}"

