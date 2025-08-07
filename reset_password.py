import tkinter as tk
from tkinter import messagebox
import sqlite3

class ResetPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Reset Password")
        self.root.state("zoomed")
        self.root.config(bg="#e8f5e9")

        tk.Label(self.root, text="Reset Your Password", font=("Arial", 26, "bold"),
                 bg="#2e7d32", fg="white", pady=20).pack(fill=tk.X)

        frame = tk.Frame(self.root, bg="#e8f5e9")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(frame, text="Username:", font=("Arial", 16), bg="#e8f5e9").grid(row=0, column=0, pady=10, sticky="e")
        self.username_entry = tk.Entry(frame, font=("Arial", 16))
        self.username_entry.grid(row=0, column=1, pady=10)

        tk.Label(frame, text="Registered Email:", font=("Arial", 16), bg="#e8f5e9").grid(row=1, column=0, pady=10, sticky="e")
        self.email_entry = tk.Entry(frame, font=("Arial", 16))
        self.email_entry.grid(row=1, column=1, pady=10)

        tk.Label(frame, text="New Password:", font=("Arial", 16), bg="#e8f5e9").grid(row=2, column=0, pady=10, sticky="e")
        self.new_password_entry = tk.Entry(frame, font=("Arial", 16), show="*")
        self.new_password_entry.grid(row=2, column=1, pady=10)

        reset_btn = tk.Button(frame, text="Reset Password", font=("Arial", 14, "bold"), bg="#388e3c", fg="white",
                              command=self.reset_password)
        reset_btn.grid(row=3, column=0, columnspan=2, pady=20)

        # Back to Login Button
        back_btn = tk.Button(frame, text="Back to Login", font=("Arial", 14), bg="gray", fg="white",
                             command=self.back_to_login)
        back_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def reset_password(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        new_password = self.new_password_entry.get().strip()

        if not username or not email or not new_password:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        conn = sqlite3.connect("student_data.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND email=?", (username, email))
        result = cur.fetchone()

        if result:
            cur.execute("UPDATE users SET password=? WHERE username=?", (new_password, username))
            conn.commit()
            messagebox.showinfo("Success", "Password reset successfully!")
            self.back_to_login()
        else:
            messagebox.showerror("Error", "Username and email do not match.")

        conn.close()

    def back_to_login(self):
        self.root.destroy()
        from user_login import UserLogin
        root = tk.Tk()
        UserLogin(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    ResetPassword(root)
    root.mainloop()
