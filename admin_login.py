import tkinter as tk
from tkinter import messagebox
from admin_dashboard import AdminDashboard

class AdminLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Login")
        self.root.state("zoomed")
        self.root.config(bg="#e0f7fa")

        tk.Label(self.root, text="Admin Login", font=("Arial", 30, "bold"), bg="#006064", fg="white", pady=20).pack(fill=tk.X)

        login_frame = tk.Frame(self.root, bg="white", bd=3, relief=tk.RIDGE)
        login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=500, height=300)

        # Username
        tk.Label(login_frame, text="Username:", font=("Arial", 14), bg="white").place(x=50, y=50)
        self.username_entry = tk.Entry(login_frame, font=("Arial", 14), width=25)
        self.username_entry.place(x=180, y=50)

        # Password
        tk.Label(login_frame, text="Password:", font=("Arial", 14), bg="white").place(x=50, y=110)
        self.password_entry = tk.Entry(login_frame, font=("Arial", 14), width=25, show="*")
        self.password_entry.place(x=180, y=110)

        # Buttons
        tk.Button(login_frame, text="Login", font=("Arial", 14, "bold"), bg="#006064", fg="white",
                  command=self.login).place(x=180, y=180)
        tk.Button(login_frame, text="Back", font=("Arial", 14, "bold"), bg="gray", fg="white",
                  command=self.go_back).place(x=280, y=180)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin123":
            messagebox.showinfo("Success", "Admin login successful!")
            self.root.destroy()
            dashboard_root = tk.Tk()
            AdminDashboard(dashboard_root)
            dashboard_root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid Admin credentials!")

    def go_back(self):
        self.root.destroy()
        from main_portal import MainPortal
        root = tk.Tk()
        MainPortal(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = AdminLogin(root)
    root.mainloop()
