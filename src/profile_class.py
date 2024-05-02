import pandas as pd
import csv

class Profile:
    def __init__(self, name, total_points=0, total_tasks=0, missed_deadlines=0):
        self.name = name
        self.total_points = total_points
        self.missed_deadlines = missed_deadlines
        self.completed_tasks = 0
        self.todo_tasks = 0
        self.ongoing_tasks = 0
        self.calculate_completed_tasks()
        self.calculate_todo_tasks()
        self.calculate_inprogress_tasks()

    def calculate_completed_tasks(self):
        tasklist = pd.read_csv('tasklist.csv')
        completed_tasks = tasklist[tasklist['Status'] == 'Completed']
        self.completed_tasks = len(completed_tasks)
    
    def calculate_todo_tasks(self):
        tasklist = pd.read_csv('tasklist.csv')
        todo_tasks = tasklist[tasklist['Status'] == 'To Do']
        self.todo_tasks = len(todo_tasks)
    
    def calculate_inprogress_tasks(self):
        tasklist = pd.read_csv('tasklist.csv')
        inprogress_tasks = tasklist[tasklist['Status'] == 'In Progress']
        self.inprogress_tasks = len(inprogress_tasks)
    
    def calculate_missed_deadlines(self):
        # TODO: Implement this function
        return 0
    
    def to_dict(self):
        return {
            'name': self.name,
            'total_points': self.total_points,
            'missed_deadlines': self.missed_deadlines,
            'completed_tasks': self.completed_tasks,
            'todo_tasks': self.todo_tasks,
            'ongoing_tasks': self.inprogress_tasks
        }
    
    @staticmethod
    def from_dict(data):
        name = data['name']
        total_points = data['total_points']
        completed_tasks = data['completed_tasks']
        inprogress_tasks = data['inprogress_tasks']
        missed_deadlines = data['missed_deadlines']
        profile = Profile(name, total_points, completed_tasks, inprogress_tasks, missed_deadlines)
        return profile

    def __str__(self):
        return f"Name: {self.name}\nTotal Points: {self.total_points}\nCompleted Tasks: {self.completed_tasks}\nMissed Deadlines: {self.missed_deadlines}\nTodo Tasks: {self.todo_tasks}\nIn Progress Tasks: {self.inprogress_tasks}"



# Test the profile functions
# profile = Profile("Name Surname")
# print(profile)
