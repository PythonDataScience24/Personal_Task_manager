from datetime import datetime
import sys
sys.path.append('src')


from taskValidator import taskValidator
import unittest
import pandas as pd
import sys
import json
import os
from unittest.mock import patch, MagicMock
from manager import Manager

# open tests: complete_task() / filter() 
# Notes -> test_AddCategory doesnt work but logic of AddCategory probably flawed as it tries to add a new
# row to the tasklist with just the category. it probably should initialize a seperate Category_List or be cut.

class TestManager(unittest.TestCase):
    @patch.object(Manager, 'create_tasklist')
    def test_innit(self, mock_create_tasklist):

        testmanager = Manager()

        #Asserts
        assert testmanager.file_path == 'tasklist.csv'
        mock_create_tasklist.assert_called_once()

    
    @patch('os.path.exists')
    @patch.object(pd, 'read_csv')
    def test_createtasklist_exists(self, mock_exists, mock_read_csv):
        #if path
        mock_exists.return_value = True

        testManager = Manager()
        #asserts
        mock_read_csv.assert_called_once()
    
    @patch.object(pd.DataFrame, 'to_csv')
    @patch('pandas.DataFrame')
    @patch('os.path.exists')
    def test_createtasklist_creates(self, mock_exists, mock_DataFrame, mock_to_csv):
        #else path
        mock_exists.return_value = False

        #mock to_csv and return a mock Dataframe
        mock_DataFrame.return_value = MagicMock(spec=pd.DataFrame)
        mock_DataFrame_instance = mock_DataFrame.return_value
        mock_DataFrame_instance.to_csv = MagicMock()

        testManager = Manager()

        #Asserts
        mock_DataFrame.assert_called_once_with(columns=["Title", "Description", "Deadline", "Category", "Priority", "Status", "Completion Time", "Duration Planned", "Duration", "Points"])
        mock_DataFrame_instance.to_csv.assert_called_once_with(testManager.file_path, index=False)
        
    def dfSetUp(self):
        self.dfTest = pd.DataFrame(columns=
                              ["Title", "Description", "Deadline", "Category", "Priority", "Status",
                                "Completion Time", "Duration Planned", "Duration", "Points"])

    @patch.object(pd, 'read_csv')
    @patch('os.path.exists')
    @patch.object(pd.DataFrame, 'to_csv')
    def test_add_task(self, mock_to_csv, mock_csv_exists, mock_read_csv):
        
        mock_csv_exists.return_value = True
        manager = Manager()
        mock_to_csv.to_csv = MagicMock()
        self.dfSetUp()
        manager.tasklist = self.dfTest
        
        #initialize Task
        manager.add_task(title='A' , description="A", deadline= "1.1.2025", category='A',
                         status="To Do", duration_planned=20)
        #try to add completed Task
        with self.assertRaises(ValueError) as context:
            manager.add_task(status='Completed')
        #add an in Progress task
        with patch.object(manager, 'set_inprogress') as mock_set_inprogress:
            manager.add_task(status='In Progress')
            mock_set_inprogress.assert_called_once()
             
        #Assertions
        ColumnValues = ['A', 'A', pd.to_datetime('2025-01-01 00:00:00'), 'A', 0, "To Do", None, 20, None, None]
        i = 0
        row = self.dfTest.iloc[0]
        for column_name, value in row.items():
            assert ColumnValues[i] == value
            i = i + 1

    @patch.object(pd, 'read_csv')
    @patch('os.path.exists')
    @patch.object(pd.DataFrame, 'to_csv')    
    def test_edit_task(self, mock_to_csv, mock_csv_exists, mock_read_csv):
        
        mock_csv_exists.return_value = True
        manager = Manager()
        mock_to_csv.to_csv = MagicMock()
        self.dfSetUp()
        manager.tasklist = self.dfTest

        manager.add_task(title='A' , description="A", deadline= "1.1.2025", category='A',
                         status="To Do", duration_planned=20)

        manager.edit_task(i=0, title='B', description="B", deadline= "1.1.2026", category='B', priority=3,
                         completion_time= '1.1.2027', duration_planned=40 ,duration= 40, points=40)
        
        #Assertions
        ColumnValues = ['B', 'B', pd.to_datetime('2026-01-01 00:00:00'), 'B', 3, "To Do", pd.to_datetime('2027-01-01 00:00:00') , 40, 40, 40]
        i = 0
        row = self.dfTest.iloc[0]
        for column_name, value in row.items():
            assert ColumnValues[i] == value
            i = i + 1

    @patch('builtins.print')
    @patch.object(pd, 'read_csv')
    @patch('os.path.exists')
    @patch.object(pd.DataFrame, 'to_csv')    
    def test_delete(self, mock_to_csv, mock_csv_exists, mock_read_csv, mock_print):
        
        mock_csv_exists.return_value = True
        manager = Manager()
        mock_to_csv.to_csv = MagicMock()
        self.dfSetUp()
        manager.tasklist = self.dfTest

        manager.add_task(title='A' , description="A", deadline= "1.1.2025", category='A',
                         status="To Do", duration_planned=20)
        manager.add_task(title='B' , description="B", deadline= "1.1.2025", category='B',
                         status="To Do", duration_planned=20)
        
        manager.delete_task(i=0)
        manager.delete_task(i=10)
        mock_print.assert_called_with("Index out of range.")
        assert len(manager.tasklist) > 0
        assert manager.tasklist.iloc[0]['Title'] == 'B'
        
    @patch.object(pd, 'read_csv')
    @patch('os.path.exists')
    @patch.object(pd.DataFrame, 'to_csv')    
    def test_order_by(self, mock_to_csv, mock_csv_exists, mock_read_csv):
        
        mock_csv_exists.return_value = True
        manager = Manager()
        mock_to_csv.to_csv = MagicMock()
        self.dfSetUp()
        manager.tasklist = self.dfTest

        manager.add_task(title='B' , description="A", deadline= "1.1.2025", priority=0, category='A',
                         status="To Do", duration_planned=20, points=100)
        manager.add_task(title='A' , description="B", deadline= "1.1.2026", priority=3, category='B',
                         status="To Do", duration_planned=25, points=50)
        manager.tasklist[0, 'Status'] = 'Completed'
        
        df = manager.order_by('Title')
        assert df.iloc[0]['Title'] == 'A'

        df = manager.order_by('Deadline')
        assert df.iloc[0]['Deadline'] == pd.to_datetime('1.1.2025')

        df = manager.order_by('Category', False)
        assert df.iloc[0]['Category'] == 'B'

        df = manager.order_by('Priority')
        assert  df.iloc[0]['Priority'] == 0

        df = manager.order_by('Status', False)
        assert df.iloc[0]['Status'] == 'To Do'

        df = manager.order_by('Duration Planned', False)
        assert df.iloc[0]['Duration Planned'] == 25

        df = manager.order_by('i')
        assert df.iloc[0]['Title'] == 'B'

        df = manager.order_by('Points')
        assert df.iloc[0]['Points'] == 50

    #This test should currently not succeed because Categories doesnt work + is currently operating under another logic 
    @patch.object(pd, 'read_csv')
    @patch('os.path.exists')
    @patch.object(pd.DataFrame, 'to_csv')    
    def test_newCategory(self, mock_to_csv, mock_csv_exists, mock_read_csv):
        
        mock_csv_exists.return_value = True
        manager = Manager()
        mock_to_csv.to_csv = MagicMock()
        self.dfSetUp()
        manager.tasklist = self.dfTest

        manager.add_task(title='B' , description="A", deadline= "1.1.2025", priority=0, category='A',
                         status="To Do", duration_planned=20, points=100)
        manager.add_task(title='A' , description="B", deadline= "1.1.2026", priority=3, category='B',
                         status="To Do", duration_planned=25, points=50)
        
        categories = manager.addCategory('C')

        existingCategories = ['A','B','C']
        i = 0
        for category in categories:
            assert category == existingCategories[i]
            i = i + 1
    
    @patch.object(pd, 'read_csv')
    @patch('os.path.exists')
    @patch.object(pd.DataFrame, 'to_csv') 
    def test_set_inProgress(self, mock_to_csv, mock_csv_exists, mock_read_csv):

        mock_csv_exists.return_value = True
        manager = Manager()
        mock_to_csv.to_csv = MagicMock()
        self.dfSetUp()
        manager.tasklist = self.dfTest

        #reset return value
        mock_csv_exists.return_value = False

        manager.add_task(title='A' , description="A", deadline= "1.1.2025", priority=3, category='B',
                         status="To Do", duration_planned=25)
        manager.add_task(title='B' , description="B", deadline= "1.1.2025", priority=3, category='A',
                         status="To Do", duration_planned=25)
        #first call of the method through edit task
        manager.edit_task(0, status='In Progress')
        
        #second call
        #change value because json got created on first iteration
        mock_csv_exists.return_value = True
        manager.edit_task(1, status='In Progress')
        
        assert manager.tasklist.iloc[0]['Status'] == 'In Progress'
        assert manager.tasklist.iloc[1]['Status'] == 'In Progress'
        
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M")
        
        expectedData = [
                {
        "id": 0,
        "time": formatted_time
        },
        {
        "id": 1,
        "time": formatted_time
        }
        ]

        with open('timestamps.json', 'r') as file:
            data = json.load(file)
        
        self.assertEqual(data, expectedData)


    @patch.object(taskValidator, 'validateDeadline')
    @patch.object(pd, 'read_csv')
    @patch('os.path.exists')
    @patch.object(pd.DataFrame, 'to_csv') 
    def test_complete_task(self, mock_to_csv, mock_csv_exists, mock_read_csv, mock_validateDeadline):
        
        mock_validateDeadline.return_value = None
        mock_csv_exists.return_value = True
        
        manager = Manager()
        mock_to_csv.to_csv = MagicMock()
        self.dfSetUp()
        manager.tasklist = self.dfTest

        manager.add_task(title='A' , description="A", priority=3, category='B',
                         status="To Do", duration_planned=25)
        manager.add_task(title='B' , description="B", priority=3, category='A',
                         status="To Do", duration_planned=25)
        exampleData = [
        {
        "id": 0,
        "time": "2024-05-10 13:40"
        },
        {
        "id": 1,
        "time": "2024-05-10 13:45"
        }
        ]

        with open('timestamps.json', 'w') as file:
                json.dump(exampleData, file, indent=4)
        
        manager.edit_task(1, status='Completed')

        assert manager.tasklist.iloc[1]['Status'] == 'Completed'
        assert manager.tasklist.iloc[1]['Duration'] != None
        assert manager.tasklist.iloc[1]['Points'] != None


    @patch.object(taskValidator, 'validateDeadline')
    @patch.object(pd, 'read_csv')
    @patch('os.path.exists')
    @patch.object(pd.DataFrame, 'to_csv')  
    def test_filter(self, mock_to_csv, mock_csv_exists, mock_read_csv, mock_validateDeadline):   
        
        mock_validateDeadline.return_value = None
        mock_csv_exists.return_value = True
        
        manager = Manager()
        mock_to_csv.to_csv = MagicMock()
        self.dfSetUp()
        manager.tasklist = self.dfTest

        manager.add_task(title='A' , description="A", priority=3, category='B',
                         status="To Do", duration_planned=25)
        manager.add_task(title='B' , description="B", priority=3, category='A',
                         status="To Do", duration_planned=25)
        manager.add_task(title='C' , description="B", priority=3, category='A',
                         status="To Do", duration_planned=25)
        
        filtered1 = manager.filter(Status = 'To Do')
        assert len(filtered1) == 3
        
        filtered2 = manager.filter(Title='C')
        assert len(filtered2) == 1
        assert filtered2.iloc[0]['Title'] == 'C'

        filtered3 = manager.filter(Status = 'To Do', Title='C')
        assert len(filtered3) == 1
        assert filtered2.iloc[0]['Title'] == 'C'


