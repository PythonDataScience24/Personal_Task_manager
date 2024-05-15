import tkinter as tk
from manager import Manager
from profile_class import Profile

class TaskWidget(tk.Frame):
    def __init__(self, parent, task, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.task = task
        self.task_title = task['Title']
        self.detail_visible = False
        self.config(bg="white", height=50)
        self.create_widgets()
        self.pack(fill=tk.X, pady=2)

    def create_widgets(self):
        self.task_label = tk.Label(self, text=self.task_title, bg="white")
        self.task_label.pack(fill=tk.X, padx=10, pady=5)
        self.task_label.bind("<Button-1>", self.toggle_details)

        # Adds color code based on priority
        colors_palette = {
            1: 'green',
            2: 'yellow',
            3: 'red'
        }
        priority_color = colors_palette.get(self.task['Priority'], 'light grey')

        self.details_frame = tk.Frame(self, bg="light grey", height=50)
        self.details_label = tk.Label(self.details_frame, text=f"{self.task['Description']} - {self.task['Priority']} - {self.task['Deadline']}", bg=priority_color)
        self.details_label.pack(padx=10, pady=5)

    def toggle_details(self, event):
        if self.detail_visible:
            self.details_frame.pack_forget()
            self.detail_visible = False
        else:
            self.details_frame.pack(fill=tk.X, after=self.task_label)
            self.detail_visible = True

class TodoApp(tk.Tk):
    def __init__(self, manager, profile):
        super().__init__()
        self.manager = manager
        self.profile = profile
        self.title("TaskTask")
        self.geometry("600x500")
        self.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        top_bar = tk.Frame(self, bg="blue", height=50)
        top_bar.pack(fill=tk.X)

        tasks_btn = tk.Button(top_bar, text="Tasks", command=self.show_tasks)
        tasks_btn.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=5)

        statistics_btn = tk.Button(top_bar, text="Statistics", command=self.show_statistics)
        statistics_btn.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=5)

        # Profile button
        profile_button = tk.Button(top_bar, text="Profile", command=self.show_profile)
        profile_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Profile information
        self.profile_info_label = tk.Label(self, text="", justify="left")

        # Filter bar section
        filter_bar = tk.Frame(self, bg="grey", height=50)
        filter_bar.pack(fill=tk.X)

        # Setup for filters
        self.filters = {"Priority": tk.StringVar(), "Category": tk.StringVar(), "Status": tk.StringVar()}

        #options for the different filters
        priority_options = {"Any", '0', '1', '2', '3'}
        category_options = {"Any","Work", "Home", "Study", "Personal", "Health"} #need maybe an dynamic creation
        status_options = {"Any", "To Do", "In Progress", "Completed"}

        options_map = {
            "Priority" : priority_options,
            "Category" : category_options,
            "Status" : status_options
        }

        for f, var in self.filters.items():
            var.set("Select " + f)
            dropdown = tk.OptionMenu(filter_bar, var, *options_map[f]) 
            dropdown.pack(side=tk.LEFT, padx=10, pady=5)
            var.trace("w", lambda *_, key=f: self.apply_filters(key))

        self.tasks_section = tk.Frame(self, bg="white")
        self.tasks_section.pack(fill=tk.BOTH, expand=True)

        self.tasks_canvas = tk.Canvas(self.tasks_section)
        self.tasks_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.tasks_scrollbar = tk.Scrollbar(self.tasks_section, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tasks_canvas.configure(yscrollcommand=self.tasks_scrollbar.set)

        self.tasks_frame = tk.Frame(self.tasks_canvas, bg="white")
        self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="nw")
        self.tasks_frame.bind('<Configure>', lambda e: self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all")))

        self.statistics_section = tk.Frame(self, bg="white")
        self.statistics_section.pack(fill=tk.BOTH, expand=True)
        self.statistics_section.pack_forget()

        self.load_tasks()

    def load_tasks(self, tasks=None):
        if tasks is None:
            tasks = self.manager.get_tasklist()
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        for _, task in tasks.iterrows():
            task_widget = TaskWidget(self.tasks_frame, task)

            # Add delete button
            delete_button = tk.Button(task_widget, text="Delete", command=lambda t=task: self.delete_task(t))
            delete_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def apply_filters(self, key):
        filters = {k: v.get() for k, v in self.filters.items() if v.get() != "Select " + k and v.get() != 'Any'}
        filtered_tasks = self.manager.filter(**filters)
        self.load_tasks(filtered_tasks)

    def show_tasks(self):
        self.tasks_section.pack(fill=tk.BOTH, expand=True)
        self.statistics_section.pack_forget()

    def show_statistics(self):
        self.tasks_section.pack_forget()
        self.statistics_section.pack(fill=tk.BOTH, expand=True)

    def show_profile(self):
        if not self.profile_info_label.winfo_ismapped():
            profile_info = f"Username: {self.profile.name}\nScore: {self.profile.total_points}"
            self.profile_info_label.config(text=profile_info)
            self.profile_info_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        else:
            self.profile_info_label.pack_forget()

if __name__ == "__main__":
    manager = Manager()
    profile = Profile()
    app = TodoApp(manager, profile)
    app.mainloop()
