import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ResultManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management")
        self.root.state("zoomed")
        self.root.config(bg="#e8f5e9")

        tk.Label(self.root, text="Result Management", font=("Arial", 28, "bold"),
                 bg="#2e7d32", fg="white", pady=20).pack(fill=tk.X)

        frame = tk.Frame(self.root, bg="white", bd=3, relief=tk.RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=700, height=500)

        # Username
        tk.Label(frame, text="Username:", font=("Arial", 14), bg="white").place(x=50, y=50)
        self.username_entry = tk.Entry(frame, font=("Arial", 14), width=30)
        self.username_entry.place(x=200, y=50)

        # Subject
        tk.Label(frame, text="Subject:", font=("Arial", 14), bg="white").place(x=50, y=100)
        self.subject_entry = tk.Entry(frame, font=("Arial", 14), width=30)
        self.subject_entry.place(x=200, y=100)

        # Marks
        tk.Label(frame, text="Marks:", font=("Arial", 14), bg="white").place(x=50, y=150)
        self.marks_entry = tk.Entry(frame, font=("Arial", 14), width=30)
        self.marks_entry.place(x=200, y=150)

        # Grade
        tk.Label(frame, text="Grade:", font=("Arial", 14), bg="white").place(x=50, y=200)
        self.grade_entry = tk.Entry(frame, font=("Arial", 14), width=30)
        self.grade_entry.place(x=200, y=200)

        # Buttons
        tk.Button(frame, text="Add Result", font=("Arial", 14, "bold"), bg="#388e3c", fg="white",
                  command=self.add_result).place(x=200, y=260)

        tk.Button(frame, text="View Results", font=("Arial", 14, "bold"), bg="#1b5e20", fg="white",
                  command=self.view_results).place(x=350, y=260)

        tk.Button(self.root, text="Back", font=("Arial", 14, "bold"), bg="gray", fg="white",
                  command=self.go_back).place(relx=0.5, rely=0.93, anchor=tk.CENTER)

    def add_result(self):
        username = self.username_entry.get()
        subject = self.subject_entry.get()
        marks = self.marks_entry.get()
        grade = self.grade_entry.get()

        if not username or not subject or not marks or not grade:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        conn = sqlite3.connect("student_data.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        if not cur.fetchone():
            messagebox.showerror("Error", "Username not found!")
            conn.close()
            return

        cur.execute("INSERT INTO results (username, subject, marks, grade) VALUES (?, ?, ?, ?)",
                    (username, subject, marks, grade))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Result added for {username} in {subject}")

    def view_results(self):
        top = tk.Toplevel(self.root)
        top.title("All Results")
        top.geometry("600x400")
        top.config(bg="white")

        tree = ttk.Treeview(top, columns=("username", "subject", "marks", "grade"), show="headings")
        tree.heading("username", text="Username")
        tree.heading("subject", text="Subject")
        tree.heading("marks", text="Marks")
        tree.heading("grade", text="Grade")
        tree.pack(fill=tk.BOTH, expand=True)

        conn = sqlite3.connect("student_data.db")
        cur = conn.cursor()
        cur.execute("SELECT username, subject, marks, grade FROM results")
        for row in cur.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()

    def go_back(self):
        self.root.destroy()
        from admin_dashboard import AdminDashboard
        root = tk.Tk()
        AdminDashboard(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    ResultManager(root)
    root.mainloop()
