class Profile:
    def __init__(self, name, total_points=0, total_tasks=0, missed_deadlines=0): #set some default values
        self.name = name
        self.total_points = total_points
        self.total_tasks = total_tasks
        self.missed_deadlines = missed_deadlines

    def __str__(self):
        pass

