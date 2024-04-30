
#This is a very basic overview of the project with the four necessary classes and their methods.
#It can be used as a skeleton to then build upon and add more functionality to the project.

class Task:
    def __init__(self, title, description, deadline=None, category=None, priority="Medium", status="To Do", on_time=True, duration_planned=None, duration=None, points=None): #set some default values
        self.title = title
        self.description = description
        self.deadline = deadline
        self.category = category
        self.priority = priority
        self.status = status
        self.on_time = on_time
        self.duration_planned = duration_planned
        self.duration = duration
        self.points = points

    def __str__(self):
        pass

    def calculate_points(self):
        pass





class Profile:
    def __init__(self, name, total_points=0, total_tasks=0, missed_deadlines=0): #set some default values
        self.name = name
        self.total_points = total_points
        self.total_tasks = total_tasks
        self.missed_deadlines = missed_deadlines

    def __str__(self):
        pass






class TaskList:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        pass

    def delete_task(self, task):
        pass

    def get_task_list(self):
        pass






class TaskManager:
    def __init__(self):
        self.tasks = []

    def get_all_tasks(self):
        pass

    def get_task_by_title(self, title):
        pass

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


