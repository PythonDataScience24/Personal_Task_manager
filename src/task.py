class Task:
    def __init__(self, title, description, deadline=None, category=None, priority="Medium", status="To Do", completion_time=True, duration_planned=None, duration=None, points=None): #set some default values
        self.title = title
        self.description = description
        self.deadline = deadline
        self.category = category
        self.priority = priority
        self.status = status
        self.completion_time = completion_time
        self.duration_planned = duration_planned
        self.duration = duration
        self.points = points

    def __str__(self):
        pass

    def calculate_points(self):
        pass
