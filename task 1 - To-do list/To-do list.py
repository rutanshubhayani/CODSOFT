import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Colorful Task Organizer")
root.geometry("300x400")
root.configure(bg="#eaf6fb")  # Light blue background

# 📝 Title label
title_label = tk.Label(root, text="🗂️ My To-Do List", font=("Arial", 14, "bold"), bg="#eaf6fb")
title_label.pack(pady=(10, 0))

# 🧾 Entry box
entry = tk.Entry(root, width=28, font=("Arial", 10))
entry.pack(pady=10)

# 📄 Listbox
listbox = tk.Listbox(root, width=30, height=10, font=("Arial", 10))
listbox.pack(pady=5)

# ➕ Add Task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# ✏️ Edit Task
def update_task():
    try:
        selected_index = listbox.curselection()[0]
        new_task = entry.get()
        if new_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except:
        messagebox.showwarning("Warning", "You must select a task to update.")

# 🗑️ Delete Task
def remove_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# ✅ Add Button
add_button = tk.Button(root, text="➕ Add Task", bg="#4CAF50", fg="white",
                       font=("Arial", 10, "bold"), command=add_task)
add_button.pack(pady=(10, 4), ipadx=10, ipady=2)

# ✏️ Edit Button
edit_button = tk.Button(root, text="✏️ Edit Task", bg="#2196F3", fg="white",
                        font=("Arial", 10, "bold"), command=update_task)
edit_button.pack(pady=4, ipadx=12, ipady=2)

# ❌ Delete Button
delete_button = tk.Button(root, text="🗑️ Delete Task", bg="#f44336", fg="white",
                          font=("Arial", 10, "bold"), command=remove_task)
delete_button.pack(pady=4, ipadx=6, ipady=2)

# Run the app
root.mainloop()
