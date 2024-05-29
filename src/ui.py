import tkinter as tk
from manager import Manager
from profile_class import Profile
from visualizer import Visualizer
from taskValidator import taskValidator
from tkinter import messagebox
from tkcalendar import Calendar
import datetime as dt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

class TaskWidget(tk.Frame):
    def __init__(self, parent, task, row, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.task = task
        self.task_title = task['Title']
        self.detail_visible = False
        self.config(bg="white", height=50, bd=1, relief=tk.RAISED)
        self.task_status = task['Status']
        self.idx = row
        self.color_status = 'light grey'
        self.create_widgets()
        self.pack(fill=tk.X, pady=2)
        
    def create_widgets(self):
        self.task_label = tk.Label(self, text=self.task_title, bg="white")
        self.task_label.pack(fill=tk.X, padx=10, pady=5)
        self.task_label.bind("<Button-1>", self.toggle_details)

        # Add colors to the status label
        colors_palette_status = {
            'To Do': 'red',
            'In Progress': 'yellow',
            'Completed': 'green'
        }

        self.color_status = colors_palette_status.get(self.task_status, 'light grey')
        
        self.status_label = tk.Label(self, text=self.task_status, bg=self.color_status)
        self.status_label.pack(fill=tk.X, padx=10, pady=5)
        self.status_label.bind("<Button-1>", self.change_status)

        # Add color code based on priority
        colors_palette_priority = {
            1: 'green',
            2: 'yellow',
            3: 'red'
        }
        priority_color = colors_palette_priority.get(self.task['Priority'], 'light grey')

        self.details_frame = tk.Frame(self, bg="light grey", height=50)
        self.details_label = tk.Label(self.details_frame, text=f"Description: {self.task['Description']}", bg=priority_color)
        self.details_label.pack(padx=10, pady=5, fill="x")

        self.details_label = tk.Label(self.details_frame, text=f"Priority: {self.task['Priority']}", bg=priority_color)
        self.details_label.pack(padx=10, pady=5, fill="x")

        self.details_label = tk.Label(self.details_frame, text=f"Deadline: {self.task['Deadline']}", bg=priority_color)
        self.details_label.pack(padx=10, pady=5, fill="x")


    def toggle_details(self, event):
        if self.detail_visible:
            self.details_frame.pack_forget()
            self.detail_visible = False
        else:
            self.details_frame.pack(fill=tk.X, after=self.task_label)
            self.detail_visible = True
    
    def change_status(self, event):
        if self.task_status == 'To Do':
            manager.edit_task(self.idx, status='In Progress')
            self.task_status = 'In Progress'
            self.color_status = 'yellow'
        elif self.task_status == 'In Progress':
            manager.edit_task(self.idx, status='Completed')
            self.task_status = 'Completed'
            self.color_status = 'green'
  
        self.status_label.config(text=self.task_status, bg=self.color_status)

class TodoApp(tk.Tk):
    def __init__(self, manager, profile):
        super().__init__()
        self.manager = manager
        self.profile = profile
        self.title("TaskTask")
        self.geometry("800x500")
        self.resizable(True, True)
        self.profile_panel = None
        self.create_widgets()

    def create_widgets(self):
        top_bar = tk.Frame(self, bg="royalblue", height=70, pady=10)
        top_bar.pack(fill=tk.X)
        
        button_font = ("Arial", 16, "bold")
        button_hover_bg = "skyblue" 

        tasks_btn = tk.Button(top_bar, text="Tasks", command=self.show_tasks, font=button_font)
        tasks_btn.pack(side=tk.LEFT, fill=tk.BOTH, padx=20)
        tasks_btn.bind("<Enter>", lambda e: tasks_btn.configure(bg=button_hover_bg))
        tasks_btn.bind("<Leave>", lambda e: tasks_btn.configure(bg="royalblue"))

        statistics_btn = tk.Button(top_bar, text="Statistics", command=self.show_statistics, font=button_font)
        statistics_btn.pack(side=tk.LEFT, fill=tk.BOTH, padx=20)
        statistics_btn.bind("<Enter>", lambda e: statistics_btn.configure(bg=button_hover_bg))
        statistics_btn.bind("<Leave>", lambda e: statistics_btn.configure(bg="royalblue"))

        # Profile button
        profile_button = tk.Button(top_bar, text="Profile", command=self.show_profile, font=button_font)
        profile_button.pack(side=tk.RIGHT, padx=20)
        profile_button.bind("<Enter>", lambda e: profile_button.configure(bg=button_hover_bg))
        profile_button.bind("<Leave>", lambda e: profile_button.configure(bg="royalblue"))


        # Filter bar section
        filter_bar = tk.Frame(self, bg="lightgray", height=50)
        filter_bar.pack(fill=tk.X)

        # Setup for filters
        self.filters = {"Priority": tk.StringVar(), "Category": tk.StringVar(), "Status": tk.StringVar()}

        # Options for the different filters
        priority_options = {"Any", '0', '1', '2', '3'}
        category_options = {"Any", "Work", "Home", "Study", "Personal", "Health"}
        status_options = {"Any", "To Do", "In Progress", "Completed"}

        options_map = {
            "Priority": priority_options,
            "Category": category_options,
            "Status": status_options
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

        # Add Task button
        add_task_button = tk.Button(top_bar, text="+", command=self.open_add_task_dialog, font=("Arial", 18, "bold"), bg="green")
        add_task_button.pack(side=tk.RIGHT, padx=10, pady=5)

        self.load_tasks()

    def load_tasks(self, tasks=None):
        if tasks is None:
            tasks = self.manager.get_tasklist()
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        for row, task in tasks.iterrows():
            task_widget = TaskWidget(self.tasks_frame, task, row)

            # Add delete button
            delete_button = tk.Button(task_widget, text="Delete", command=lambda idx=row: self.delete_task(idx))
            delete_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def apply_filters(self, key):
        filters = {k: v.get() for k, v in self.filters.items() if v.get() != "Select " + k and v.get() != 'Any'}
        filtered_tasks = self.manager.filter(**filters)
        self.load_tasks(filtered_tasks)

    def open_add_task_dialog(self):
        # Create a new window for adding tasks
        self.add_task_window = tk.Toplevel(self.master)
        self.add_task_window.title("Add Task")
        self.add_task_window.geometry("400x400")

        # Labels and entry fields for task details
        tk.Label(self.add_task_window, text="Title:").pack()
        self.title_entry = tk.Entry(self.add_task_window)
        self.title_entry.pack()

        tk.Label(self.add_task_window, text="Description:").pack()
        self.description_entry = tk.Entry(self.add_task_window)
        self.description_entry.pack()

        # Priority label and dropdown menu in the same line
        priority_frame = tk.Frame(self.add_task_window)
        priority_frame.pack()
        tk.Label(priority_frame, text="Priority:").pack(side='left')
        # Dropdown menu for priority selection
        self.priority_var = tk.StringVar(self.add_task_window)
        self.priority_var.set("0")  # Default value
        priority_options = ["0", "1", "2", "3"]
        self.priority_menu = tk.OptionMenu(priority_frame, self.priority_var, *priority_options)
        self.priority_menu.pack(side='left')
        
        # Category label and dropdown menu in the same line
        category_frame = tk.Frame(self.add_task_window)
        category_frame.pack()
        tk.Label(category_frame, text="Category:").pack(side='left')
        self.category_var = tk.StringVar(self.add_task_window)
        predefined_categories = ["Home", "Work", "Study", "Personal", "Health"]
        self.category_menu = tk.OptionMenu(category_frame, self.category_var, *predefined_categories)
        self.category_menu.pack(side='left')

        # Deadline section
        tk.Label(self.add_task_window, text="Deadline:").pack()

        tomorrow = dt.date.today() + dt.timedelta(days=1)  # Add 1 day to get tomorrow's date

        self.deadline_calendar = Calendar(self.add_task_window, selectmode='day',
                                        date_pattern='dd.mm.yyyy',
                                        year=tomorrow.year, month=tomorrow.month,
                                        day=tomorrow.day,
                                        mindate=tomorrow,  # Set mindate to tomorrow
                                        foreground='black')  # Set font color to black
        self.deadline_calendar.pack()
        
        # Planned duration section
        duration_frame = tk.Frame(self.add_task_window)
        duration_frame.pack()
        tk.Label(duration_frame, text="Planned Duration:").pack()

        hours_frame = tk.Frame(self.add_task_window)
        hours_frame.pack()
        tk.Label(hours_frame, text="Hours:").pack(side='left')
        self.hours_entry = tk.Spinbox(hours_frame, from_=0, to=23, width=5)
        self.hours_entry.pack(side='left')

        # Button to submit the task
        submit_button = tk.Button(self.add_task_window, text="Add Task", command=self.submit_task)
        submit_button.pack()

    def submit_task(self):
        # Get task details from entry fields
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_var.get()
        category = self.category_var.get()
        deadline = self.deadline_calendar.get_date()
        planned_duration = self.hours_entry.get()
        
        planned_duration = float(planned_duration)
        formatted_duration = f"{planned_duration:.1f}"  # Format to one decimal place

        # Validate task details
        if not title or not deadline:
            messagebox.showerror("Error", "Please fill in both title and deadline fields.")
            return

        # Add the task using manager
        self.manager.add_task(
            title=title,
            description=description,
            deadline=deadline,
            category=category,
            priority=priority,
            duration_planned=formatted_duration 
        )
         # Close the add task window after successful addition
        self.add_task_window.destroy()
        self.load_tasks()

    def delete_task(self, rowidx):
        self.manager.delete_task(rowidx)
        self.load_tasks()

    def show_tasks(self):
        self.tasks_section.pack(fill=tk.BOTH, expand=True)
        self.statistics_section.pack_forget()
        self.load_tasks()

    def show_statistics(self):
        self.tasks_section.pack_forget()
        self.statistics_section.pack(fill=tk.BOTH, expand=True)

        for widget in self.statistics_section.winfo_children():
            widget.destroy()

        tk.Button(self.statistics_section, text="Tasks Statistics", command=self.visualize_category_tasks_statistics).pack(pady=5)
        tk.Button(self.statistics_section, text="Times and Points Statistics", command=self.visualize_points_statistics).pack(pady=5)

    def visualize_category_tasks_statistics(self):
        for widget in self.statistics_section.winfo_children():
            widget.destroy()
        frame1 = tk.Frame(self.statistics_section)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        Visualizer.tasks_by_priority_and_category_pie(self.manager.get_tasklist(), frame1)
        
        frame2 = tk.Frame(self.statistics_section)
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        Visualizer.tasks_by_priority_and_category(self.manager.get_tasklist(), frame2)

    def visualize_points_statistics(self):
        for widget in self.statistics_section.winfo_children():
            widget.destroy()
        frame1 = tk.Frame(self.statistics_section)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        Visualizer.upcoming_deadlines(self.manager.get_tasklist(), frame1)
        
        frame2 = tk.Frame(self.statistics_section)
        frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        Visualizer.points_over_time(self.manager.get_tasklist(), frame2)

    def create_profile_panel(self):
        self.profile_panel = tk.Frame(self, bg="lightgrey", width=250, padx=10, pady=10)
        self.profile_panel.pack(side=tk.BOTTOM, fill=tk.X)

        close_button = tk.Button(self.profile_panel, text="✕", command=self.close_profile_panel, bg="white", fg="black", bd=0, font=("Arial", 12))
        close_button.pack(anchor=tk.NE)

        profile_info = f"Name: {self.profile.name}\nTotal Points: {self.profile.total_points}"
        tk.Label(self.profile_panel, text="Profile", font=("Arial", 14, "bold"), bg="lightgrey").pack(anchor=tk.NW, pady=(0, 10))
        ttk.Separator(self.profile_panel, orient='horizontal').pack(fill='x', pady=(0, 10))

        tk.Label(self.profile_panel, text=profile_info, justify="left", bg="lightgrey").pack(anchor=tk.NW)

        # Icons representing tasks
        tasks_frame = tk.Frame(self.profile_panel, bg="lightgrey")
        tasks_frame.pack(pady=(10, 0))

        completed_icon = tk.Label(tasks_frame, text="✓", font=("Arial", 12), bg="lightgrey")
        completed_icon.grid(row=0, column=0, padx=(10, 5))

        completed_label = tk.Label(tasks_frame, text=f"Completed: {self.profile.completed_tasks}", bg="lightgrey")
        completed_label.grid(row=0, column=1)

        todo_icon = tk.Label(tasks_frame, text="⚑", font=("Arial", 12), bg="lightgrey")
        todo_icon.grid(row=1, column=0, padx=(10, 5))

        todo_label = tk.Label(tasks_frame, text=f"To Do: {self.profile.todo_tasks}", bg="lightgrey")
        todo_label.grid(row=1, column=1)

        inprogress_icon = tk.Label(tasks_frame, text="➔", font=("Arial", 12), bg="lightgrey")
        inprogress_icon.grid(row=2, column=0, padx=(10, 5))

        inprogress_label = tk.Label(tasks_frame, text=f"In Progress: {self.profile.inprogress_tasks}", bg="lightgrey")
        inprogress_label.grid(row=2, column=1)



    def show_profile(self):
        if self.profile_panel and self.profile_panel.winfo_ismapped():
            self.profile_panel.pack_forget()
        else:
            if not self.profile_panel:
                self.create_profile_panel()
            else:
                self.profile_panel.pack(side=tk.BOTTOM, fill=tk.X)

    def close_profile_panel(self):
        if self.profile_panel is not None:
            self.profile_panel.pack_forget()

if __name__ == "__main__":
    manager = Manager()
    profile = Profile()
    app = TodoApp(manager=manager, profile=profile)
    app.mainloop()


