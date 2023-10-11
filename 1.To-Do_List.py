# To design a To-Do List applicationn using Python, allowing users to create, update, and track their to-do lists.

import tkinter as tk

app_width = 400
app_height = 750

# Function to add a task-

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to remove a task-

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

# To design the interface-

app = tk.Tk()
app.title("To-Do List")
app.geometry(f"{app_width}x{app_height}")

# To add a task-

add_button = tk.Button(app, text="Add Task", command=add_task, width=15, font=8)
add_button.pack(pady=5)

task_entry = tk.Entry(app, width=30, font=8)
task_entry.pack(pady=10)

# To remove a task-

remove_button = tk.Button(app, text="Remove Task", command=remove_task, width=15, font=8)
remove_button.pack(pady=10)

# To view the list of tasks-

task_list = tk.Listbox(app, width=30, height=22, font=8)
task_list.pack(pady=10)

# Main loop-

app.mainloop()
