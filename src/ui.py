import tkinter as tk

root = tk.Tk()
root.title("TaskTask")

root.geometry("600x500")
root.resizable(False, False)

# Create top bar
top_bar = tk.Frame(root, bg="gray", height=50)
top_bar.pack(fill=tk.X)

# Create buttons for sections
tasks_btn = tk.Button(top_bar, text="Tasks", padx=10)
tasks_btn.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=5)

statistics_btn = tk.Button(top_bar, text="Statistics", padx=10)
statistics_btn.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=5)

# Create section for tasks
tasks_section = tk.Frame(root, bg="white")
tasks_section.pack(fill=tk.BOTH, expand=True)

# Create example list of tasks
tasks_list = tk.Listbox(tasks_section, bg="white", selectbackground="lightgray")
tasks_list.pack(fill=tk.BOTH, expand=True)

# Add example entries to the list
tasks_list.insert(tk.END, "Task 1")
tasks_list.insert(tk.END, "Task 2")
tasks_list.insert(tk.END, "Task 3")
tasks_list.insert(tk.END, "Task 4")

# Create section for statistics
statistics_section = tk.Frame(root, bg="white")
statistics_section.pack(fill=tk.BOTH, expand=True)

# Hide statistics section initially
statistics_section.pack_forget()

# Function to switch to tasks section
def show_tasks():
    tasks_section.pack(fill=tk.BOTH, expand=True)
    statistics_section.pack_forget()

# Function to switch to statistics section
def show_statistics():
    tasks_section.pack_forget()
    statistics_section.pack(fill=tk.BOTH, expand=True)

# Configure button commands
tasks_btn.configure(command=show_tasks)
statistics_btn.configure(command=show_statistics)

# Start the application
root.mainloop()
