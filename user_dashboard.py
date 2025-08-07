import tkinter as tk
from tkinter import *
import sqlite3

class UserDashboard:
    def __init__(self, root, username):
        self.root = root
        self.root.title("User Dashboard")
        self.root.state("zoomed")
        self.root.config(bg="#f1f8e9")
        self.username = username

        Label(self.root, text=f"Welcome, {self.username}", font=("Arial", 30, "bold"), bg="#558b2f", fg="white", pady=20).pack(fill=X)

        frame = Frame(self.root, bg="#f1f8e9")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        Button(frame, text="View Attendance", font=("Arial", 16, "bold"), width=25, bg="#7cb342", fg="white",
               command=self.view_attendance).grid(row=0, column=0, padx=20, pady=20)

        Button(frame, text="View Results", font=("Arial", 16, "bold"), width=25, bg="#558b2f", fg="white",
               command=self.view_results).grid(row=1, column=0, padx=20, pady=20)

        Button(frame, text="View Profile", font=("Arial", 16, "bold"), width=25, bg="#33691e", fg="white",
               command=self.view_profile).grid(row=2, column=0, padx=20, pady=20)

        Button(self.root, text="Logout", font=("Arial", 14, "bold"), bg="red", fg="white", width=15,
               command=self.logout).place(relx=0.5, rely=0.9, anchor=CENTER)

    def view_attendance(self):
        self.new_window("Attendance", "SELECT date, status FROM attendance WHERE username=?")

    def view_results(self):
        self.new_window("Results", "SELECT subject, marks, grade FROM results WHERE username=?")

    def view_profile(self):
        self.new_window("Profile", "SELECT name, email FROM users WHERE username=?")

    def new_window(self, title, query):
        win = Toplevel(self.root)
        win.title(title)
        win.geometry("500x400")
        win.config(bg="white")

        frame = Frame(win, bg="white")
        frame.pack(fill=BOTH, expand=True)

        conn = sqlite3.connect("student_data.db")
        cur = conn.cursor()
        cur.execute(query, (self.username,))
        records = cur.fetchall()
        conn.close()

        for idx, row in enumerate(records):
            for col, val in enumerate(row):
                Label(frame, text=str(val), font=("Arial", 12), bg="white", anchor=W).grid(row=idx, column=col, padx=10, pady=5)

    def logout(self):
        self.root.destroy()
        from main_portal import MainPortal
        root = tk.Tk()
        MainPortal(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    UserDashboard(root, "sample_user")
    root.mainloop()
