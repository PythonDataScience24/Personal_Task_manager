from manager import Manager


manager = Manager()
manager.create_tasklist()
#manager.add_task("Task1", "Description1", "2021-12-31", "Work", "High", "To Do", True, 2, 2, 10)
manager.delete_task(0)

manager.edit_task(1, title="Task2", description="HELLO,WORLD")
manager.print_tasklist()