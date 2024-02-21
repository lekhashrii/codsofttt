import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create and place widgets
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=1, column=0, columnspan=2, pady=10)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()

