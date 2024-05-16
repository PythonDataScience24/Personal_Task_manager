# Fixing Profile Class with Pylint

## Introduction

In this document, we'll discuss how to improve the quality of the `profile_class.py` file by addressing the issues identified by Pylint.

---

## Pylint Output Before Fixing

```plaintext
************* Module profile_class
profile_class.py:25:0: C0303: Trailing whitespace (trailing-whitespace)    
profile_class.py:29:0: C0303: Trailing whitespace (trailing-whitespace)    
profile_class.py:33:0: C0303: Trailing whitespace (trailing-whitespace)    
profile_class.py:38:0: C0301: Line too long (137/100) (line-too-long)      
profile_class.py:40:0: C0303: Trailing whitespace (trailing-whitespace)    
profile_class.py:50:0: C0303: Trailing whitespace (trailing-whitespace)    
profile_class.py:59:0: C0301: Line too long (107/100) (line-too-long)      
profile_class.py:88:0: C0301: Line too long (186/100) (line-too-long)      
profile_class.py:90:0: C0304: Final newline missing (missing-final-newline)
profile_class.py:1:0: C0114: Missing module docstring (missing-module-docstring)
profile_class.py:6:0: C0115: Missing class docstring (missing-class-docstring)
profile_class.py:22:4: C0116: Missing function or method docstring (missing-function-docstring)
profile_class.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)
profile_class.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
profile_class.py:34:4: C0116: Missing function or method docstring (missing-function-docstring)
profile_class.py:41:4: C0116: Missing function or method docstring (missing-function-docstring)
profile_class.py:51:4: C0116: Missing function or method docstring (missing-function-docstring)
-function-docstring)
profile_class.py:2:0: W0611: Unused import csv (unused-import)
profile_class.py:2:0: C0411: standard import "import csv" should be placed before "import pandas as pd" (wrong-import-order)
profile_class.py:3:0: C0411: standard import "import json" should be placed before "import pandas as pd" (wrong-import-order)
profile_class.py:4:0: C0411: standard import "import os" should be placed before "import pandas as pd" (wrong-import-order)
-----------------------------------
Your code has been rated at 6.27/10
```

## Fixing Trailing Whitespace Issues, Adding docstrings for each method

```plaintext
************* Module profile_class
profile_class.py:79:0: C0303: Trailing whitespace (trailing-whitespace)
profile_class.py:83:0: C0303: Trailing whitespace (trailing-whitespace)
profile_class.py:93:0: C0301: Line too long (107/100) (line-too-long)
profile_class.py:130:0: C0301: Line too long (186/100) (line-too-long)
profile_class.py:1:0: C0114: Missing module docstring (missing-module-docstring)

------------------------------------------------------------------
Your code has been rated at 9.14/10 (previous run: 1.60/10, +7.54)
```


# Fixing manager class with pylint

## Pylint output before fixing 
```plaintext
************* Module manager
manager.py:18:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:25:0: C0301: Line too long (181/100) (line-too-long)
manager.py:29:0: C0301: Line too long (178/100) (line-too-long)
manager.py:32:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:33:0: C0301: Line too long (253/100) (line-too-long)
manager.py:38:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:40:0: C0301: Line too long (193/100) (line-too-long)
manager.py:52:0: C0301: Line too long (105/100) (line-too-long)
manager.py:60:0: C0301: Line too long (108/100) (line-too-long)
manager.py:66:0: C0301: Line too long (104/100) (line-too-long)
manager.py:80:0: C0301: Line too long (101/100) (line-too-long)
manager.py:106:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:107:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:108:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:124:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:129:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:134:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:150:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:158:0: C0301: Line too long (116/100) (line-too-long)
manager.py:160:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:164:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:166:0: C0301: Line too long (118/100) (line-too-long)
manager.py:170:89: C0303: Trailing whitespace (trailing-whitespace)
manager.py:172:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:174:101: C0303: Trailing whitespace (trailing-whitespace)
manager.py:174:0: C0301: Line too long (101/100) (line-too-long)
manager.py:178:0: C0301: Line too long (105/100) (line-too-long)
manager.py:180:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:189:16: C0303: Trailing whitespace (trailing-whitespace)
manager.py:197:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:216:0: C0303: Trailing whitespace (trailing-whitespace)
manager.py:217:0: C0305: Trailing newlines (trailing-newlines)
manager.py:1:0: C0114: Missing module docstring (missing-module-docstring)
manager.py:12:0: C0115: Missing class docstring (missing-class-docstring)
manager.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:29:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:29:4: R0913: Too many arguments (11/5) (too-many-arguments)
manager.py:34:8: E1101: Instance of 'TextFileReader' has no 'to_csv' member (no-member)
manager.py:40:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:40:4: R0913: Too many arguments (12/5) (too-many-arguments)
manager.py:41:11: R1716: Simplify chained comparison between the operands (chained-comparison)      
manager.py:47:16: E1101: Instance of 'TextFileReader' has no 'at' member (no-member)
manager.py:50:16: E1101: Instance of 'TextFileReader' has no 'at' member (no-member)
manager.py:53:16: E1101: Instance of 'TextFileReader' has no 'at' member (no-member)
manager.py:56:16: E1101: Instance of 'TextFileReader' has no 'at' member (no-member)
manager.py:59:16: E1101: Instance of 'TextFileReader' has no 'at' member (no-member)
manager.py:66:16: E1101: Instance of 'TextFileReader' has no 'at' member (no-member)
manager.py:68:16: E1101: Instance of 'TextFileReader' has no 'at' member (no-member)
manager.py:70:16: E1101: Instance of 'TextFileReader' has no 'at' member (no-member)
manager.py:72:16: E1101: Instance of 'TextFileReader' has no 'at' member (no-member)
manager.py:73:12: E1101: Instance of 'TextFileReader' has no 'to_csv' member (no-member)
manager.py:40:4: R0912: Too many branches (14/12) (too-many-branches)
manager.py:77:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:78:11: R1716: Simplify chained comparison between the operands (chained-comparison)      
manager.py:82:12: E1101: Instance of 'TextFileReader' has no 'reset_index' member (no-member)
manager.py:83:12: E1101: Instance of 'TextFileReader' has no 'to_csv' member (no-member)
manager.py:87:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:90:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:91:11: R1716: Simplify chained comparison between the operands (chained-comparison)      
manager.py:90:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
manager.py:120:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:121:11: R1716: Simplify chained comparison between the operands (chained-comparison)     
manager.py:127:22: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
manager.py:120:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
manager.py:156:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:158:12: C0103: Variable name "sortedbyTitle_df" doesn't conform to snake_case naming style (invalid-name)
manager.py:162:12: C0103: Variable name "sortedbyDeadline_df" doesn't conform to snake_case naming style (invalid-name)
manager.py:162:34: E1101: Instance of 'TextFileReader' has no 'sort_values' member (no-member)
manager.py:166:12: C0103: Variable name "sortedbyCategory_df" doesn't conform to snake_case naming style (invalid-name)
manager.py:166:34: E1101: Instance of 'TextFileReader' has no 'sort_values' member (no-member)
manager.py:170:12: C0103: Variable name "sortedbyPriority_df" doesn't conform to snake_case naming style (invalid-name)
manager.py:170:34: E1101: Instance of 'TextFileReader' has no 'sort_values' member (no-member)
manager.py:174:12: C0103: Variable name "sortedbyStatus_df" doesn't conform to snake_case naming style (invalid-name)
manager.py:174:32: E1101: Instance of 'TextFileReader' has no 'sort_values' member (no-member)
manager.py:178:12: C0103: Variable name "sortedbyDurationPlanned_df" doesn't conform to snake_case naming style (invalid-name)
manager.py:178:41: E1101: Instance of 'TextFileReader' has no 'sort_values' member (no-member)
manager.py:182:12: C0103: Variable name "sortedbyIndex_df" doesn't conform to snake_case naming style (invalid-name)
manager.py:182:31: E1101: Instance of 'TextFileReader' has no 'sort_index' member (no-member)
manager.py:186:12: C0103: Variable name "sortedbyPoints_df" doesn't conform to snake_case naming style (invalid-name)
manager.py:186:32: E1101: Instance of 'TextFileReader' has no 'sort_values' member (no-member)
manager.py:156:4: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
manager.py:156:4: R0911: Too many return statements (8/6) (too-many-return-statements)
manager.py:190:4: C0103: Method name "addCategory" doesn't conform to snake_case naming style (invalid-name)
manager.py:190:4: C0103: Argument name "newCategory" doesn't conform to snake_case naming style (invalid-name)
manager.py:190:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:199:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:202:28: E1101: Instance of 'TextFileReader' has no 'columns' member (no-member)
manager.py:208:4: C0103: Method name "upcomingDeadlines" doesn't conform to snake_case naming style (invalid-name)
manager.py:208:4: C0116: Missing function or method docstring (missing-function-docstring)
manager.py:2:0: C0411: standard import "import os" should be placed before "import pandas as pd" (wrong-import-order)
manager.py:4:0: C0411: standard import "from datetime import datetime" should be placed before "import pandas as pd" (wrong-import-order)
manager.py:5:0: C0411: standard import "import json" should be placed before "import pandas as pd" (wrong-import-order)

------------------------------------
Your code has been rated at -2.66/10
```

## 1. Remove Trailing Whitespaces

** Removed trailing whitespace from lines 18, 25, 32, 38, 40, 106, 107, 108, 124, 129, 134, 150, 158, 160, 164, 170, 172, 174 **

For example: 
```python
# Before
class Manager:
    def __init__(self):
        self.file_path = "tasklist.csv"
        self.create_tasklist()
        
# After
class Manager:
    def __init__(self):
        self.file_path = "tasklist.csv"
        self.create_tasklist()
```

## 2. Refactor lines that are too long
** Refactored lines 25, 29, 33, 40, 52, 60, 66, 80 to fit within the 100-character limit.** 

For example:
```python
# Before
def edit_task(self, i: int, title=None, description=None, deadline=None, category=None, priority=None, status=None, completion_time=None, duration_planned=None, duration=None, points=None):

# After
def edit_task(self, i: int, title=None, description=None, deadline=None, category=None, 
              priority=None, status=None, completion_time=None, duration_planned=None, 
              duration=None, points=None):
```

## 3. Include missing Docstrings
** Added module docstring at the beginning of the file.**

```python
# Before (no change)

# After
"""
This module defines the Manager class for managing tasks.
"""
```

## 4. Iclude missing Class Docstrings and method Docstrings
** Added Docstrings at the beginning of the class and of each method** 

For example: 
```python
# Before (no change)

# After
def create_tasklist(self):
    """
    Create or load the tasklist.
    """
```

## 5. Refactor methods with too many arguments
** Refactor the methods add_task and edit_task so that they take in less arguments**

```python
# Previous Code
...
    def add_task(self, title='', description="", deadline='', category=None, priority=0, status="To Do", completion_time=None, duration_planned=None, duration=None, points=None):
        ...

# Improved Code
...
    def add_task(self, task):
        """Adds a task to the task list."""
        title = task.get("title", "")
        description = task.get("description", "")
        deadline = task.get("deadline", "")
        category = task.get("category", None)
        priority = task.get("priority", 0)
        status = task.get("status", "To Do")
        completion_time = task.get("completion_time", None)
        duration_planned = task.get("duration_planned", None)
        duration = task.get("duration", None)
        points = task.get("points", None)
        ...

# Previous Code
...
    def edit_task(self, i: int, title=None, description=None, deadline=None, category=None, priority=None, status=None, completion_time=None, duration_planned=None, duration=None, points=None):
        ...

# Improved Code
...
    def edit_task(self, i: int, task_changes):
        """Edits an existing task in the task list."""
        if i < len(self.tasklist) and i >= 0:
            task = self.tasklist.iloc[i].copy()
            task.update(task_changes)

            title = task.get("title", None)
            description = task.get("description", None)
            deadline = task.get("deadline", None)
            category = task.get("category", None)
            priority = task.get("priority", None)
            status = task.get("status", None)
            completion_time = task.get("completion_time", None)
            duration_planned = task.get("duration_planned", None)
            duration = task.get("duration", None)
            points = task.get("points", None)

            self.tasklist.at[i, "Title"] = title if title is not None else self.tasklist.at[i, "Title"]
            self.tasklist.at[i, "Description"] = description if description is not None else self.tasklist.at[i, "Description"]
            self.tasklist.at[i, "Deadline"] = taskValidator.validateDeadline(deadline) if deadline is not None else self.tasklist.at[i, "Deadline"]
            self.tasklist.at[i, "Category"] = category if category is not None else self.tasklist.at[i, "Category"]
            self.tasklist.at[i, "Priority"] = taskValidator.validatePriority(priority) if priority is not None else self.tasklist.at[i, "Priority"]
            self.tasklist.at[i, "Status"] = taskValidator.validateStatus(status) if status is not None else self.tasklist.at[i, "Status"]
            self.tasklist.at[i, "Completion Time"] = taskValidator.validateDeadline(completion_time) if completion_time is not None else self.tasklist.at[i, "Completion Time"]
            self.tasklist.at[i, "Duration Planned"] = duration_planned if duration_planned is not None else self.tasklist.at[i, "Duration Planned"]
            self.tasklist.at[i, "Duration"] = duration if duration is not None else self.tasklist.at[i, "Duration"]
            self.tasklist.at[i, "Points"] = points if points is not None else self.tasklist.at[i, "Points"]

            self.tasklist.to_csv(self.file_path, index=False)
        else:
            print("Index out of range.")
        ...
```

## 6. Fixing 'E1101: Instance of 'TextFileReader' has no 'at' member (no-member)'
**By adding a .read() after pd.read_csv() so that the argument returns a Dataframe and not a TextFileReader**

```python
    def create_tasklist(self):
        """Create a tasklist."""
        if os.path.exists(self.file_path):
            self.tasklist = pd.read_csv(self.file_path).read()  # Add .read() here
            print("File found and loaded into a dataframe.")
        else:
            self.tasklist = pd.DataFrame(columns=["Title", "Description", "Deadline", "Category", "Priority", "Status", "Completion Time", "Duration Planned", "Duration", "Points"])
            self.tasklist.to_csv(self.file_path, index=False)
            print("File not found. Created a new empty dataframe.")
```

## 7. Simplify chained arguments

```python
# Before
if i < len(self.tasklist) and i >= 0:

# After
if 0 <= i < len(self.tasklist):
```

