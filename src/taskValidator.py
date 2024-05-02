import datetime as dt

class TaskValidator:

    #to do but maybe its more usefull if we know which kind of input the user is able to give?
    class TaskValidator:
        @staticmethod
        def validateDeadline(x):
            """
            Validates the deadline format and checks if it is in the future.

            Args:
                x (str): The deadline string in the format "%d.%m.%Y" or "%d.%m.%y" or "%d.%m".

            Returns:
                datetime.datetime or None: The validated deadline as a datetime object if it is in the future, 
                otherwise returns None.
                """
            try:
                deadline = dt.datetime.strptime(x, "%d.%m.%Y")
            except ValueError:
                try:
                    deadline = dt.datetime.strptime(x, "%d.%m.%y")
                except ValueError:
                    try:
                        deadline = dt.datetime.strptime(x, "%d.%m")
                        current_year = dt.datetime.now().year
                        if deadline.day < dt.datetime.now().day:
                            deadline = deadline.replace(year=current_year + 1)
                        else:
                            deadline = deadline.replace(year=current_year)
                    except ValueError:
                        print("Invalid deadline format")
                        return None
            
            if deadline < dt.datetime.now():
                print("Deadline cannot be in the past")
                return None
            
            return deadline

        @staticmethod
        def validatePriority(x):
            #priority has to be either 0,1,2,3
            if x < 0:
                return 0
            if x > 3:
                return 3
            else:
                return x
    
        @staticmethod
        def validateStatus(x):
            #status has to be either "To Do", "In Progress", "Completed"
            valid_statuses = ["To Do", "In Progress", "Completed"]
            if x in valid_statuses:
                return x
            else:
                print("Status is not valid.")
                return None
   
