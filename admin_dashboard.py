import tkinter as tk
from tkinter import *
from attendance_management import AttendanceManager
from result_management import ResultManager
from profile_management import ProfileManager

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.state("zoomed")
        self.root.config(bg="#e8f5e9")

        title = Label(self.root, text="Admin Dashboard", font=("Arial", 30, "bold"), bg="#1b5e20", fg="white", pady=20)
        title.pack(fill=X)

        frame = Frame(self.root, bg="#e8f5e9")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        Button(frame, text="Attendance Management", font=("Arial", 16, "bold"), width=25, bg="#43a047", fg="white",
               command=self.attendance).grid(row=0, column=0, padx=20, pady=20)

        Button(frame, text="Result Management", font=("Arial", 16, "bold"), width=25, bg="#2e7d32", fg="white",
               command=self.result).grid(row=1, column=0, padx=20, pady=20)

        Button(frame, text="User Profile Management", font=("Arial", 16, "bold"), width=25, bg="#388e3c", fg="white",
               command=self.profile).grid(row=2, column=0, padx=20, pady=20)

        Button(self.root, text="Logout", font=("Arial", 14, "bold"), bg="red", fg="white", width=15,
               command=self.logout).place(relx=0.5, rely=0.9, anchor=CENTER)

    def attendance(self):
        self.root.destroy()
        root = tk.Tk()
        AttendanceManager(root)
        root.mainloop()

    def result(self):
        self.root.destroy()
        root = tk.Tk()
        ResultManager(root)
        root.mainloop()

    def profile(self):
        self.root.destroy()
        root = tk.Tk()
        ProfileManager(root)
        root.mainloop()

    def logout(self):
        self.root.destroy()
        from main_portal import MainPortal
        root = tk.Tk()
        MainPortal(root)
        root.mainloop()




if __name__ == "__main__":
    root = tk.Tk()
    AdminDashboard(root)
    root.mainloop()
