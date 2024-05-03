import unittest
import pandas as pd
from profile_class import Profile
import json
import os

class TestProfile(unittest.TestCase):
    def setUp(self):
        self.profile = Profile('Test', total_points=0)
        self.profile.tasklist = pd.read_csv('tasklist.csv')
        self.profile.tasklist['Deadline'] = pd.to_datetime(self.profile.tasklist['Deadline'])


    def test_total_tasks(self):
        self.profile.calculate_completed_tasks()
        self.profile.calculate_todo_tasks()
        self.profile.calculate_inprogress_tasks()
        total_tasks = self.profile.completed_tasks + self.profile.todo_tasks + self.profile.inprogress_tasks
        self.assertEqual(len(self.profile.tasklist), total_tasks)

    def test_calculate_total_points(self):
        self.profile.calculate_total_points()
        self.assertEqual(self.profile.total_points, self.profile.tasklist['Points'].sum())

    def test_to_dict(self):
        profile_dict = self.profile.to_dict()
        self.assertEqual(profile_dict['name'], self.profile.name)
        self.assertEqual(profile_dict['total_points'], self.profile.total_points)
        self.assertEqual(profile_dict['completed_tasks'], self.profile.completed_tasks)
        self.assertEqual(profile_dict['todo_tasks'], self.profile.todo_tasks)
        self.assertEqual(profile_dict['ongoing_tasks'], self.profile.inprogress_tasks)

    def test_save_to_json(self):
        self.profile.save_to_json('test.json')
        with open('test.json', 'r') as file:
            data = json.load(file)
        self.assertEqual(data[0]['name'], self.profile.name)
        os.remove('test.json')

    # def test_update_and_save(self)
    #...


    def test_str(self):
        profile_str = str(self.profile)
        self.assertIn(self.profile.name, profile_str)
        self.assertIn(str(self.profile.total_points), profile_str)
        self.assertIn(str(self.profile.completed_tasks), profile_str)
        self.assertIn(str(self.profile.todo_tasks), profile_str)
        self.assertIn(str(self.profile.inprogress_tasks), profile_str)

    # def test_calculate_missed_deadlines(self):
    #     self.profile.tasklist = pd.read_csv('tasklist.csv')
    #     self.profile.tasklist['Deadline'] = pd.to_datetime(self.profile.tasklist['Deadline'])
    #     self.profile.calculate_missed_deadlines()
    #     self.assertEqual(self.profile.missed_deadlines, 2)

if __name__ == '__main__':
    unittest.main()