import tkinter as tk
from tkinter import *

class MainPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.state("zoomed")
        self.root.config(bg="#f0f0f0")

        title = Label(self.root, text="Welcome to Student Management System", font=("Arial", 30, "bold"), bg="#003366", fg="white", pady=20)
        title.pack(fill=X)

        btn_frame = Frame(self.root, bg="#f0f0f0")
        btn_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Buttons
        Button(btn_frame, text="Admin Portal", width=20, height=2, font=("Arial", 16, "bold"), bg="#0052cc", fg="white",
               command=self.open_admin).grid(row=0, column=0, padx=20, pady=20)

        Button(btn_frame, text="User Login", width=20, height=2, font=("Arial", 16, "bold"), bg="#007f5f", fg="white",
               command=self.open_user_login).grid(row=0, column=1, padx=20, pady=20)

        Button(btn_frame, text="User Registration", width=20, height=2, font=("Arial", 16, "bold"), bg="#ffc300", fg="black",
               command=self.open_register).grid(row=1, column=0, columnspan=2, pady=20)

        Button(self.root, text="Exit", width=15, font=("Arial", 14, "bold"), bg="red", fg="white",
               command=self.root.quit).place(relx=0.5, rely=0.9, anchor=CENTER)

    def open_admin(self):
        self.root.destroy()
        from admin_login import AdminLogin
        new_root = tk.Tk()
        AdminLogin(new_root)
        new_root.mainloop()


    def open_user_login(self):
        self.root.destroy()
        from user_login import UserLogin
        new_root = tk.Tk()
        UserLogin(new_root)
        new_root.mainloop()

    def open_register(self):
        self.root.destroy()
        from user_register import UserRegister
        new_root = tk.Tk()
        UserRegister(new_root)
        new_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainPortal(root)
    root.mainloop()
