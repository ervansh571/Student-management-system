import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import date

class AttendanceManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management")
        self.root.state("zoomed")
        self.root.config(bg="#fffde7")

        tk.Label(self.root, text="Attendance Management", font=("Arial", 28, "bold"),
                 bg="#fbc02d", fg="black", pady=20).pack(fill=tk.X)

        frame = tk.Frame(self.root, bg="white", bd=3, relief=tk.RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=700, height=500)

        # Username Entry
        tk.Label(frame, text="Username:", font=("Arial", 14), bg="white").place(x=50, y=50)
        self.username_entry = tk.Entry(frame, font=("Arial", 14), width=30)
        self.username_entry.place(x=200, y=50)

        # Status Dropdown
        tk.Label(frame, text="Status:", font=("Arial", 14), bg="white").place(x=50, y=100)
        self.status_combo = ttk.Combobox(frame, font=("Arial", 14), state="readonly", width=28)
        self.status_combo['values'] = ("Present", "Absent", "Leave")
        self.status_combo.place(x=200, y=100)

        # Mark Attendance
        tk.Button(frame, text="Mark Attendance", font=("Arial", 14, "bold"), bg="#f9a825", fg="white",
                  command=self.mark_attendance).place(x=200, y=160)

        # View Attendance
        tk.Button(frame, text="View Records", font=("Arial", 14, "bold"), bg="#f57f17", fg="white",
                  command=self.view_records).place(x=370, y=160)

        # Back Button
        tk.Button(self.root, text="Back", font=("Arial", 14, "bold"), bg="gray", fg="white",
                  command=self.go_back).place(relx=0.5, rely=0.93, anchor=tk.CENTER)

    def mark_attendance(self):
        username = self.username_entry.get()
        status = self.status_combo.get()
        today = str(date.today())

        if not username or not status:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        conn = sqlite3.connect("student_data.db")
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        if not cur.fetchone():
            messagebox.showerror("Error", "Username not found!")
            conn.close()
            return

        cur.execute("INSERT INTO attendance (username, date, status) VALUES (?, ?, ?)",
                    (username, today, status))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Attendance marked for {username} on {today}")

    def view_records(self):
        top = tk.Toplevel(self.root)
        top.title("Attendance Records")
        top.geometry("500x400")
        top.config(bg="white")

        conn = sqlite3.connect("student_data.db")
        cur = conn.cursor()
        cur.execute("SELECT username, date, status FROM attendance")
        records = cur.fetchall()
        conn.close()

        tree = ttk.Treeview(top, columns=("username", "date", "status"), show="headings")
        tree.heading("username", text="Username")
        tree.heading("date", text="Date")
        tree.heading("status", text="Status")
        tree.pack(fill=tk.BOTH, expand=True)

        for row in records:
            tree.insert("", tk.END, values=row)

    def go_back(self):
        self.root.destroy()
        from admin_dashboard import AdminDashboard
        root = tk.Tk()
        AdminDashboard(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    AttendanceManager(root)
    root.mainloop()
