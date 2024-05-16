from manager import Manager
import random
from datetime import datetime, timedelta
import pandas as pd

def random_date():
    #generate date in next 2 years
    start_date = datetime.now()
    end_date = start_date + timedelta(days=365 * 2)
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%d.%m.%Y")

def testset():
    # possible values
    categories = ["Work", "Home", "Study", "Personal", "Health"]
    priorities = [0,1,2,3,4,5]
    statuses = ["To Do", "In Progress"]
    titles = ["A","B","a","b","c","C"]

    # 50 Random Inputs
    for i in range(50):
        task_name = random.choice(titles)
        description = f"Description{i+1}"
        due_date = random_date()
        category = random.choice(categories)
        priority = random.choice(priorities)
        status = random.choice(statuses)
        flag = random.choice([True, False])
        num1 = random.randint(1, 5) 
        num2 = random.randint(1, 5)
        num3 = random.randint(1, 20)

        manager.add_task(task_name, description, due_date, category, priority, status, flag, num1, num2, num3)

#create
manager = Manager()
manager.create_tasklist()
testset()

#orderby tests (can also be used to test ValidateTask class)
# print(manager.order_by('Title'))
#print(manager.order_by('Category'))
# print(manager.order_by('Priority', False))
# print(manager.order_by('Status', False))
#print(manager.order_by('i'))



#create, add and delete tests
#manager.add_task("Task1", "Description1", "2021-12-31", "Work", "High", "To Do", True, 2, 2, 10)
#manager.delete_task(0)
#manager.edit_task(1, title="Task2", description="HELLO,WORLD")
#manager.print_tasklist()

#test filter()
# print(manager.filter(Title = 'a'))
# print(manager.filter(Title = 'b'))
# print(manager.filter(Status = 0))


#Reserve code

    # def calculate_points(self):
    #     if self.duration is not None and self.priority is not None:
    #         duration_value = round((self.duration).int)
    #         priority_values = {0:1, 1:10, 2:6, 3:2}[self.priority]
    #         self.points = duration_value * priority_values
    #     else:
    #         self.points = None

    # def __str__(self):
    #     task_info = f"Title: {self.title}\nDescription: {self.description}\n"
    #     if self.deadline:
    #         task_info += f"Deadline: {self.deadline}\n"
    #     if self.category:
    #         task_info += f"Category: {self.category}\n"
    #     task_info += f"Priority: {self.priority}\nStatus: {self.status}\n"
    #     if self.completion_time:
    #         task_info += "Completion time: True\n"
    #     if self.duration_planned:
    #         task_info += f"Planned duration: {self.duration_planned}\n"
    #     if self.duration:
    #         task_info += f"Actual duration: {self.duration}\n"
    #     if self.points:
    #         task_info += f"Points: {self.points}\n"
    #     return task_info







