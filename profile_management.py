import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ProfileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("User Profile Management")
        self.root.state("zoomed")
        self.root.config(bg="#e3f2fd")

        tk.Label(self.root, text="User Profile Management", font=("Arial", 28, "bold"),
                 bg="#1976d2", fg="white", pady=20).pack(fill=tk.X)

        self.tree = ttk.Treeview(self.root, columns=("id", "username", "name", "email"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("username", text="Username")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.load_profiles()

        tk.Button(self.root, text="Delete Selected User", font=("Arial", 14, "bold"), bg="red", fg="white",
                  command=self.delete_user).pack(pady=10)

        tk.Button(self.root, text="Back", font=("Arial", 14, "bold"), bg="gray", fg="white",
                  command=self.go_back).pack(pady=5)

    def load_profiles(self):
        conn = sqlite3.connect("student_data.db")
        cur = conn.cursor()
        cur.execute("SELECT id, username, name, email FROM users")
        records = cur.fetchall()
        conn.close()

        self.tree.delete(*self.tree.get_children())
        for row in records:
            self.tree.insert("", tk.END, values=row)

    def delete_user(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Select User", "Please select a user to delete.")
            return
        values = self.tree.item(selected, "values")
        user_id = values[0]

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete user ID {user_id}?")
        if confirm:
            conn = sqlite3.connect("student_data.db")
            cur = conn.cursor()
            cur.execute("DELETE FROM users WHERE id=?", (user_id,))
            conn.commit()
            conn.close()
            self.load_profiles()
            messagebox.showinfo("Deleted", "User deleted successfully.")

    def go_back(self):
        self.root.destroy()
        from admin_dashboard import AdminDashboard
        root = tk.Tk()
        AdminDashboard(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    ProfileManager(root)
    root.mainloop()
