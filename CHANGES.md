# Changes made to the code
Specifically for the classes manager and profile_class using the principles od abstarction and decomposition

## Manager Class:

### Abstraction:

1. **Refactoring `create_tasklist` method:**
   - The `create_tasklist` method now focuses only on creating the tasklist DataFrame. It abstracts the creation process, allowing other methods to simply call it whenever needed.
   - **Code Example (Previous):**
     ```python
     def create_tasklist(self):
         if os.path.exists(self.file_path):
             self.tasklist = pd.read_csv(self.file_path)
             print("File found and loaded into a dataframe.")
         else:
             self.tasklist = pd.DataFrame(columns=[
                 "Title", "Description", "Deadline", "Category",
                 "Priority", "Status", "Completion Time",
                 "Duration Planned", "Duration", "Points"
             ])
             self.tasklist.to_csv(self.file_path, index=False)
             print("File not found. Created a new empty dataframe.")
     ```
   - **Code Example (Improved):**
     ```python
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
     ```

### Decomposition:

1. **Improving the `order_by` method:**
   - Removed unnecessary sorting functions from the `sort_functions` dictionary, simplifying the method and making it more focused.
   - **Code Example (Previous):**
     ```python
     def order_by(self, attribute, asc=True):
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
     ```
   - **Code Example (Improved):**
     ```python
     def order_by(self, attribute, asc=True):
         sort_functions = {
             'Title': lambda x: x.str.lower() + x,
             'Category': lambda x: x.str.lower()
         }
         if attribute in sort_functions:
             sorted_df = self.tasklist.sort_values(
                 by=attribute, ascending=asc, key=sort_functions[attribute]
             )
             return sorted_df
         else:
             print(f"Invalid attribute: {attribute}")
             return None
     ```


## Profile Class:

### Abstraction:

1. **Abstraction in Profile Class:**
   - The Profile class abstracts the user's profile information, encapsulating it in a single class.

2. **Abstraction in `to_dict` method:**
   - The `to_dict` method abstracts the conversion of a profile object into a dictionary.


### Decomposition:

1. **Separate JSON Data Loading**
     The 'save_to_json' method can be separated into a save and a loading mmethod, decomposing it.

Previous Code:
```python
def save_to_json(self, filename='profile.json'):
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
```
Improved Code:
```python
    def save_to_json(self, filename='profile.json'):
        """
        Save profile to JSON file.
        
        Args:
            filename (str): The filename to save the JSON data to. Defaults to 'profile.json'.
        """
        profile_dict = self.to_dict()
        data = self.load_json_data(filename)
        index = next((index for (index, d) in enumerate(data) if d["name"] == self.name), None)
        if index is not None:
            data[index] = profile_dict
        else:
            data.append(profile_dict)
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_json_data(filename='profile.json'):
        """
        Load JSON data from file.

        Args:
            filename (str): The filename to load the JSON data from. Defaults to 'profile.json'.

        Returns:
            list: List containing JSON data.
        """
        data = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    pass
        return data

```

2. **Decomposition in `update_and_save` method:**
   - The `update_and_save` method decomposes the tasks of updating profile attributes and saving to a JSON file into separate steps.
   - **Code Example:**
     ```python
     class Profile:
         def update_and_save(self, name=None, total_points=None):
             if name is not None:
                 self.name = name
             if total_points is not None:
                 self.total_points = total_points
             self.calculate_completed_tasks()
             self.calculate_todo_tasks()
             self.calculate_inprogress_tasks()
             self.calculate_total_points()
             self.save_to_json()
     ```

