import pandas as pd
import os




class Manager:
    def __init__(self):
        self.file_path = "tasklist.csv"

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

    def add_task(self, title, description, deadline=None, category=None, priority=0, status="To Do", completion_time=True, duration_planned=None, duration=None, points=None):
        self.tasklist.loc[len(self.tasklist)] = [title, description, deadline, category, priority, status, completion_time, duration_planned, duration, points]
        self.tasklist.to_csv(self.file_path, index=False)

    def delete_task(self, i: int):
        if i < len(self.tasklist) and i >= 0:
            self.tasklist.drop(i, inplace=True)
            self.tasklist.reset_index(drop=True, inplace=True)
            self.tasklist.to_csv(self.file_path, index=False)
        else:
            print("Index out of range.")

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
                self.tasklist.at[i, "Deadline"] = deadline
            if category:
                #needs no restriction
                # categories will get saved in a list ["Work", "Personal", "Health", "Other"] for example
                self.tasklist.at[i, "Category"] = category
            if priority:
                #either 0, 1, 2, 3
                self.tasklist.at[i, "Priority"] = priority
            if status:
                #either "To Do", "In Progress", "Completed"
                self.tasklist.at[i, "Status"] = status
            if completion_time:
                self.tasklist.at[i, "Completion Time"] = completion_time
            if duration_planned:
                self.tasklist.at[i, "Duration Planned"] = duration_planned
            if duration:
                self.tasklist.at[i, "Duration"] = duration
            if points:
                self.tasklist.at[i, "Points"] = points
            self.tasklist.to_csv(self.file_path, index=False)
        else:
            print("Index out of range.")

    def print_tasklist(self):
        print(self.tasklist)

    def complete_task(self, i: int):
        if i < len(self.tasklist) and i >= 0:
            self.edit_task(i, status="Completed")
        else:
            print("Index out of range.")

    def order_by(self, attribute, asc = True): #attribute = columns, asc = True ascending False = descending
        if attribute == 'Title':
            sortedbyTitle_df = self.tasklist.sort_values(by='Title', ascending=asc, key=lambda x: x.str.lower()) #currently A = a maybe change?
            return sortedbyTitle_df
        
        if attribute == 'Deadline':
            #first need to define datatype of Deadline
            return 0
        
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
            #first datatype needs to be defined
            return 0
        if attribute == 'i':
            sortedbyIndex_df = self.tasklist.sort_index(ascending=asc)
            return sortedbyIndex_df
        #currently only attributes which are predefined have an order_by function (missing Duration)
        if attribute == 'Points':
            sortedbyPoints_df = self.tasklist.sort_values('Points', ascending=asc)
            return sortedbyPoints_df

    def order_by_priority(self, priority):
        pass

    def order_by_deadline(self, deadline):
        pass

    def order_by_duration(self, duration):
        pass

    def order_by_points(self, points):
        pass

    def filter_by_status(self, status):
        pass

    def filter_by_category(self, category):
        pass

