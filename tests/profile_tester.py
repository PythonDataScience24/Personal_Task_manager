import unittest
import pandas as pd
import sys
import json
import os

sys.path.insert(0, 'src')
from profile_class import Profile

class TestProfile(unittest.TestCase):
    """
    Set up the test case by initializing a Profile object and loading tasklist data.
    """
    def setUp(self):
        self.profile = Profile('Test')
        self.profile.tasklist = pd.read_csv('tasklist.csv')
        self.profile.tasklist['Deadline'] = pd.to_datetime(self.profile.tasklist['Deadline'])


    """
    Test the calculation of total tasks by summing completed, todo, and in-progress tasks.
    """
    def test_total_tasks(self):
        self.profile.calculate_completed_tasks()
        self.profile.calculate_todo_tasks()
        self.profile.calculate_inprogress_tasks()
        total_tasks = self.profile.completed_tasks + self.profile.todo_tasks + self.profile.inprogress_tasks
        self.assertEqual(len(self.profile.tasklist), total_tasks)


    """
    Test the calculation of total points by summing the points of all tasks.
    """
    def test_calculate_total_points(self):
        self.profile.calculate_total_points()
        self.assertEqual(self.profile.total_points, self.profile.tasklist['Points'].sum())


    """
    Test the conversion of Profile object to a dictionary.
    """
    def test_to_dict(self):
        profile_dict = self.profile.to_dict()
        self.assertEqual(profile_dict['name'], self.profile.name)
        self.assertEqual(profile_dict['total_points'], self.profile.total_points)
        self.assertEqual(profile_dict['completed_tasks'], self.profile.completed_tasks)
        self.assertEqual(profile_dict['todo_tasks'], self.profile.todo_tasks)
        self.assertEqual(profile_dict['ongoing_tasks'], self.profile.inprogress_tasks)


    """
    Test the saving of Profile object to a JSON file and loading the data back.
    """
    def test_save_to_json(self):
        self.profile.save_to_json('tests/test.json')
        with open('tests/test.json', 'r') as file:
            data = json.load(file)
        self.assertEqual(data[0]['name'], self.profile.name)
        self.assertEqual(data[0]['total_points'], self.profile.total_points)
        self.assertEqual(data[0]['completed_tasks'], self.profile.completed_tasks)
        self.assertEqual(data[0]['todo_tasks'], self.profile.todo_tasks)
        self.assertEqual(data[0]['ongoing_tasks'], self.profile.inprogress_tasks)
        os.remove('tests/test.json')



    """
    Update the Profile object's attributes and save it to a JSON file.
    """
    #Needs some more work...
    def update_and_save(self):
        self.profile.total_points = 100
        self.profile.completed_tasks = 10
        self.profile.todo_tasks = 5
        self.profile.inprogress_tasks = 3
        self.profile.update_and_save('tests/test.json')
        with open('tests/test.json', 'r') as file:
            data= json.load(file)
            self.assertEqual(data[0]['name'], self.profile.name)
            self.assertEqual(data[0]['total_points'], self.profile.total_points)
            self.assertEqual(data[0]['completed_tasks'], self.profile.completed_tasks)
            self.assertEqual(data[0]['todo_tasks'], self.profile.todo_tasks)
            self.assertEqual(data[0]['ongoing_tasks'], self.profile.inprogress_tasks)
            os.remove('tests/test.json')


    """
    Test the string representation of the Profile object.
    """
    def test_str(self):
        profile_str = str(self.profile)
        self.assertIn(self.profile.name, profile_str)
        self.assertIn(str(self.profile.total_points), profile_str)
        self.assertIn(str(self.profile.completed_tasks), profile_str)
        self.assertIn(str(self.profile.todo_tasks), profile_str)
        self.assertIn(str(self.profile.inprogress_tasks), profile_str)

    # def test_calculate_missed_deadlines(self):

    def tear_down(self):
        #check for the test.json file and remove it
        if os.path.exists('test.json'):
            os.remove('test.json')

if __name__ == '__main__':
    unittest.main()