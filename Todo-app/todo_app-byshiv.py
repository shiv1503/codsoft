import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ---------------------- Database Setup ----------------------
def init_db():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            completed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------------------- Database Functions ----------------------
def insert_task(title, desc, due):
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)", (title, desc, due))
    conn.commit()
    conn.close()

def update_task_db(task_id, title, desc, due, completed):
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET title=?, description=?, due_date=?, completed=? WHERE id=?",
                (title, desc, due, completed, task_id))
    conn.commit()
    conn.close()

def delete_task_db(task_id):
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

def fetch_all_tasks():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks ORDER BY created_at DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

# ---------------------- Main Application ----------------------
class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List Application")
        self.geometry("900x500")
        self.configure(bg="#f5f5f5")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Title label
        title_label = tk.Label(self, text="📝 To-Do List", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Treeview styling
        style = ttk.Style()
        style.configure("Treeview", rowheight=25, font=("Arial", 10))
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
        style.map("Treeview", background=[("selected", "#cce5ff")])

        # Treeview
        self.tree = ttk.Treeview(self, columns=("No", "Title", "Due Date", "Done"), show="headings", height=15)
        self.tree.heading("No", text="No.")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.heading("Done", text="Completed")

        self.tree.column("No", width=50, anchor="center")
        self.tree.column("Title", width=250)
        self.tree.column("Due Date", width=100, anchor="center")
        self.tree.column("Done", width=100, anchor="center")

        self.tree.grid(row=1, column=0, sticky="nsew", padx=(10, 0), pady=10)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=0, sticky="nse", pady=10)

        # Button frame
        btn_frame = tk.Frame(self, bg="#f5f5f5")
        btn_frame.grid(row=1, column=1, sticky="ns", padx=10, pady=10)

        btn_style = {"width": 15, "height": 2, "font": ("Arial", 10, "bold")}
        tk.Button(btn_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", activebackground="#45a049", **btn_style).pack(pady=5)
        tk.Button(btn_frame, text="Update Task", command=self.update_task, bg="#2196F3", fg="white", activebackground="#1976D2", **btn_style).pack(pady=5)
        tk.Button(btn_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", activebackground="#e53935", **btn_style).pack(pady=5)
        tk.Button(btn_frame, text="View Details", command=self.view_details, bg="#9C27B0", fg="white", activebackground="#7B1FA2", **btn_style).pack(pady=5)

        # Status bar
        self.status_var = tk.StringVar()
        status_label = tk.Label(self, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#e0e0e0", fg="#333")
        status_label.grid(row=2, column=0, columnspan=2, sticky="ew", pady=5)

        # Load tasks initially
        self.refresh_tasks()

    # ---------------------- Task Functions ----------------------
    def refresh_tasks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = fetch_all_tasks()
        for idx, row in enumerate(rows, start=1):
            task_id, title, desc, due, completed, created = row
            due_text = due if due else '-'
            done_text = 'Yes' if completed else 'No'
            tag = "oddrow" if idx % 2 == 1 else "evenrow"
            self.tree.insert('', 'end', iid=str(task_id), values=(idx, title, due_text, done_text), tags=(tag,))

        self.tree.tag_configure("oddrow", background="#ffffff")
        self.tree.tag_configure("evenrow", background="#f0f0f0")
        self.status_var.set(f'Loaded {len(rows)} tasks')

    def add_task(self):
        TaskEditor(self, "Add Task")

    def update_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Task", "Please select a task to update.")
            return
        task_id = int(selected[0])
        TaskEditor(self, "Update Task", task_id)

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Task", "Please select a task to delete.")
            return
        task_id = int(selected[0])
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?")
        if confirm:
            delete_task_db(task_id)
            self.refresh_tasks()
            self.status_var.set("Task deleted successfully")

    def view_details(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Task", "Please select a task to view.")
            return
        task_id = int(selected[0])
        conn = sqlite3.connect("todo.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
        task = cur.fetchone()
        conn.close()

        if task:
            _, title, desc, due, completed, created = task
            details = f"Title: {title}\nDescription: {desc}\nDue Date: {due}\nCompleted: {'Yes' if completed else 'No'}\nCreated At: {created}"
            messagebox.showinfo("Task Details", details)

# ---------------------- Task Editor ----------------------
class TaskEditor(tk.Toplevel):
    def __init__(self, master, title, task_id=None):
        super().__init__(master)
        self.task_id = task_id
        self.title(title)
        self.geometry("400x300")
        self.configure(bg="#ffffff")

        tk.Label(self, text="Title:", bg="#ffffff").pack(pady=5)
        self.title_entry = tk.Entry(self, width=40)
        self.title_entry.pack(pady=5)

        tk.Label(self, text="Description:", bg="#ffffff").pack(pady=5)
        self.desc_entry = tk.Text(self, width=40, height=5)
        self.desc_entry.pack(pady=5)

        tk.Label(self, text="Due Date (YYYY-MM-DD):", bg="#ffffff").pack(pady=5)
        self.due_entry = tk.Entry(self, width=40)
        self.due_entry.pack(pady=5)

        self.completed_var = tk.IntVar()
        tk.Checkbutton(self, text="Completed", variable=self.completed_var, bg="#ffffff").pack(pady=5)

        tk.Button(self, text="Save", command=self.save_task, bg="#4CAF50", fg="white").pack(pady=10)

        if task_id:
            self.load_task()

    def load_task(self):
        conn = sqlite3.connect("todo.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE id=?", (self.task_id,))
        task = cur.fetchone()
        conn.close()

        if task:
            _, title, desc, due, completed, _ = task
            self.title_entry.insert(0, title)
            self.desc_entry.insert("1.0", desc)
            self.due_entry.insert(0, due if due else "")
            self.completed_var.set(completed)

    def save_task(self):
        title = self.title_entry.get().strip()
        desc = self.desc_entry.get("1.0", tk.END).strip()
        due = self.due_entry.get().strip()
        completed = self.completed_var.get()

        if not title:
            messagebox.showerror("Error", "Title cannot be empty")
            return

        if self.task_id:
            update_task_db(self.task_id, title, desc, due, completed)
            self.master.status_var.set("Task updated successfully")
        else:
            insert_task(title, desc, due)
            self.master.status_var.set("Task added successfully")

        self.master.refresh_tasks()
        self.destroy()

# ---------------------- Run Application ----------------------
if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
