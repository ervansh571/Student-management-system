import tkinter as tk
from tkinter import messagebox
import sqlite3
from user_dashboard import UserDashboard

class UserLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        self.root.state("zoomed")
        self.root.config(bg="#e3f2fd")

        tk.Label(self.root, text="User Login", font=("Arial", 30, "bold"), bg="#1565c0", fg="white", pady=20).pack(fill=tk.X)

        frame = tk.Frame(self.root, bg="white", bd=3, relief=tk.RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=500, height=300)

        # Username
        tk.Label(frame, text="Username:", font=("Arial", 14), bg="white").place(x=50, y=50)
        self.username_entry = tk.Entry(frame, font=("Arial", 14), width=25)
        self.username_entry.place(x=180, y=50)

        # Password
        tk.Label(frame, text="Password:", font=("Arial", 14), bg="white").place(x=50, y=110)
        self.password_entry = tk.Entry(frame, font=("Arial", 14), width=25, show="*")
        self.password_entry.place(x=180, y=110)

        # Buttons
        tk.Button(frame, text="Login", font=("Arial", 14, "bold"), bg="#1565c0", fg="white",
                  command=self.login).place(x=180, y=180)
        tk.Button(frame, text="Back", font=("Arial", 14, "bold"), bg="gray", fg="white",
                  command=self.go_back).place(x=280, y=180)
        forgot_btn = tk.Button(frame, text="Forgot Password?", font=("Arial", 12, "underline"), fg="blue",
                               bg="#f1f8e9", bd=0, cursor="hand2", command=self.open_password_reset)
        forgot_btn.place(x=200, y=235)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        conn = sqlite3.connect("student_data.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            root = tk.Tk()
            UserDashboard(root, username)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def open_password_reset(self):
        self.root.destroy()
        from reset_password import ResetPassword
        root = tk.Tk()
        ResetPassword(root)
        root.mainloop()

    def go_back(self):
        self.root.destroy()
        from main_portal import MainPortal
        root = tk.Tk()
        MainPortal(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    UserLogin(root)
    root.mainloop()
