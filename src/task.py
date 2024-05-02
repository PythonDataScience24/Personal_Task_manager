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
        task_info = f"Title: {self.title}\nDescription: {self.description}\n"
        if self.deadline:
            task_info += f"Deadline: {self.deadline}\n"
        if self.category:
            task_info += f"Category: {self.category}\n"
        task_info += f"Priority: {self.priority}\nStatus: {self.status}\n"
        if self.completion_time:
            task_info += "Completion time: True\n"
        if self.duration_planned:
            task_info += f"Planned duration: {self.duration_planned}\n"
        if self.duration:
            task_info += f"Actual duration: {self.duration}\n"
        if self.points:
            task_info += f"Points: {self.points}\n"
        return task_info


    def calculate_points(self):
        if self.duration is not None and self.priority is not None:
            duration_value = round((self.duration).int)
            priority_values = {0:1, 1:10, 2:6, 3:2}[self.priority]
            self.points = duration_value * priority_values
        else:
            self.points = None
    
