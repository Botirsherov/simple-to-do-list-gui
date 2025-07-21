import tkinter as tk
from tkinter import messagebox

TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            for line in f:
                task = line.strip()
                if task:
                    listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved to file.")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the window
root = tk.Tk()
root.title("📝 To-Do List")

# Entry for task
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

# Add Button
add_btn = tk.Button(root, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=1)

# Listbox to show tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.grid(row=1, column=0, columnspan=2, padx=10)

# Delete Button
del_btn = tk.Button(root, text="Delete Task", width=12, command=delete_task)
del_btn.grid(row=2, column=0, pady=10)

# Save Button
save_btn = tk.Button(root, text="Save Tasks", width=12, command=save_tasks)
save_btn.grid(row=2, column=1)

# Load tasks at startup
load_tasks()

# Run the GUI
root.mainloop()
