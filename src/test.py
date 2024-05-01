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
    return random_date.strftime("%Y-%m-%d")

def testset():
# possible values
    categories = ["Work", "Home", "Study", "Personal", "Health"]
    priorities = [0,1,2,3]
    statuses = ["To Do", "In Progress", "Completed"]
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

manager = Manager()
manager.create_tasklist()
#testset()

#orderby tests
#print(manager.order_by('Title'))
print(manager.order_by('Category'))
print(manager.order_by('Priority', False))
#print(manager.order_by('Status', False))
#print(manager.order_by('i'))




#manager.add_task("Task1", "Description1", "2021-12-31", "Work", "High", "To Do", True, 2, 2, 10)
#manager.delete_task(0)
#manager.edit_task(1, title="Task2", description="HELLO,WORLD")
#manager.print_tasklist()












