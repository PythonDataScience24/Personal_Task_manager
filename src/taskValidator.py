import datetime as dt

class taskValidator:
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
        # Check if x is empty or cannot be converted to an integer
        if not x.strip() or not x.strip().isdigit():
            return 0  # Return the default priority value

        # Convert x to an integer
        priority = int(x)

        # Check if priority is within the valid range
        if priority < 0:
            return 0
        elif priority > 3:
            return 3
        else:
            return priority

    @staticmethod
    def validateStatus(x):
        #status has to be either "To Do", "In Progress", "Completed"
        valid_statuses = ["to do", "in progress", "completed"]
        
        if x.strip().lower() in valid_statuses:
            return x.title().strip()
        else:
            print("Status is not valid.")
            return None
   
   
