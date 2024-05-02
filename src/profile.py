import pandas as pd


class Profile:
    def __init__(self, name, total_points=0, total_tasks=0, missed_deadlines=0):
        self.name = name
        self.total_points = total_points
        self.total_tasks = total_tasks
        self.missed_deadlines = missed_deadlines
        self.completed_tasks = self.calculate_completed_tasks()
        self.todo_tasks = self.calculate_todo_tasks()
        self.ongoing_tasks = self.calculate_ongoing_tasks()

    def calculate_completed_tasks(self):
        counter = 0
        pd.read_csv('tasklist.csv'):
                    counter += 1
        return counter
    
    def calculate_todo_tasks(self):
        counter = 0
        with open('tasklist.csv', 'r') as file:
            for line in file:
                status = line.split(',')[2].strip()
                if status == 'To Do':
                    counter += 1
        return counter

    def calculate_ongoing_tasks(self):
        counter = 0
        with open('tasklist.csv', 'r') as file:
            for line in file:
                status = line.split(',')[2].strip()
                if status == 'Ongoing':
                    counter += 1
        return counter
    
    def calculate_missed_deadlines(self):
        return self.missed_deadlines

    def __str__(self):
        return f"Name: {self.name}\nTotal Points: {self.total_points}\nTotal Tasks: {self.total_tasks}\nCompleted Tasks: {self.completed_tasks}\nMissed Deadlines: {self.missed_deadlines}\nTodo Tasks: {self.todo_tasks}\nOngoing Tasks: {self.ongoing_tasks}"



# import unittest
# from profile import Profile
# import csv

# class TestProfile(unittest.TestCase):
#     def test_profile(self):
#         profile = Profile("John Doe")
        
#         # Read values from tasklist.csv and display them
#         with open('tasklist.csv', 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 print(row)
        
#         # Display the profile
#         print("Name:", profile.name)
#         print("Total Points:", profile.total_points)
#         print("Total Tasks:", profile.total_tasks)
#         print("Missed Deadlines:", profile.missed_deadlines)
#         print("Completed Tasks:", profile.completed_tasks)
#         print("Todo Tasks:", profile.todo_tasks)
#         print("Ongoing Tasks:", profile.ongoing_tasks)

# if __name__ == '__main__':
#     unittest.main()