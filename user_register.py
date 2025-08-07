import tkinter as tk
from tkinter import messagebox
import sqlite3

class UserRegister:
    def __init__(self, root):
        self.root = root
        self.root.title("User Registration")
        self.root.state("zoomed")
        self.root.config(bg="#fce4ec")

        tk.Label(self.root, text="User Registration", font=("Arial", 30, "bold"), bg="#c2185b", fg="white", pady=20).pack(fill=tk.X)

        frame = tk.Frame(self.root, bg="white", bd=3, relief=tk.RIDGE)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=600, height=400)

        # Name
        tk.Label(frame, text="Full Name:", font=("Arial", 14), bg="white").place(x=50, y=40)
        self.name_entry = tk.Entry(frame, font=("Arial", 14), width=30)
        self.name_entry.place(x=200, y=40)

        # Email
        tk.Label(frame, text="Email:", font=("Arial", 14), bg="white").place(x=50, y=90)
        self.email_entry = tk.Entry(frame, font=("Arial", 14), width=30)
        self.email_entry.place(x=200, y=90)

        # Username
        tk.Label(frame, text="Username:", font=("Arial", 14), bg="white").place(x=50, y=140)
        self.username_entry = tk.Entry(frame, font=("Arial", 14), width=30)
        self.username_entry.place(x=200, y=140)

        # Password
        tk.Label(frame, text="Password:", font=("Arial", 14), bg="white").place(x=50, y=190)
        self.password_entry = tk.Entry(frame, font=("Arial", 14), width=30, show="*")
        self.password_entry.place(x=200, y=190)

        # Buttons
        tk.Button(frame, text="Register", font=("Arial", 14, "bold"), bg="#c2185b", fg="white",
                  command=self.register_user).place(x=200, y=260)

        tk.Button(frame, text="Back", font=("Arial", 14, "bold"), bg="gray", fg="white",
                  command=self.go_back).place(x=320, y=260)

    def register_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not all([name, email, username, password]):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        try:
            conn = sqlite3.connect("student_data.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO users (name, email, username, password) VALUES (?, ?, ?, ?)",
                        (name, email, username, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User registered successfully!")
            self.root.destroy()
            import main_portal
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")

    def go_back(self):
        self.root.destroy()
        from main_portal import MainPortal
        root = tk.Tk()
        MainPortal(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    UserRegister(root)
    root.mainloop()
