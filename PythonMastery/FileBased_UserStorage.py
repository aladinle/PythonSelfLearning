import os
import tkinter as tk
from tkinter import messagebox

FILENAME = 'users.txt'

# make sure file exists
# check if file not exist, then create it
if not os.path.exists(FILENAME):
    open(FILENAME, "w").close()

def register():
    user = entry_user.get().strip()
    password = entry_pass.get().strip()

    if not user or not password:
        messagebox.showerror("Error","Username and Password cannot be empty!")
        return

    # check if user already exist
    with open(FILENAME, "r") as f:
        for line in f:
            stored_user, _ = line.strip().split(",")
            if user == stored_user:
                messagebox.showerror("Error", "Username already exist!")
                return

    # else: save new username to file
    with open(FILENAME, "a") as f:
        f.write(f"{user},{password}\n")
    messagebox.showinfo("Success","Register successfully!")
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)

def login():
    user = entry_user.get().strip()
    password = entry_pass.get().strip()

    if not os.path.exists(FILENAME):
        messagebox.showerror("Error","No users registered yet!")
        return

    # else
    with open(FILENAME, "r") as f:
        for line in f:
            stored_user, stored_pass = line.strip().split(",")
            if user == stored_user and password == stored_pass:
                messagebox.showinfo("Welcome", f"Login successful! Welcome,{user}")
                return
    # else, username or password does not match
    messagebox.showerror("Error", "Invalid username or password!")

def forgot_password_action(event=None):
    messagebox.showinfo("Forgot Password", "Password reset feature coming soon!")
def help_action():
    messagebox.showinfo("Help Center", "Please call 1-800-333-4447 for help\nor email letrung87@gmail.com.")
def contact_action():
    messagebox.showinfo("Contact Us", "Email: support@mysite.com")

# -------------- tkinter UI -----------------
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

# Labels Username
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_user = tk.Entry(root)
entry_user.grid(row=0,column=1, padx=10, pady=5)

# Labels Password
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_pass = tk.Entry(root, show="*")
entry_pass.grid(row=1, column=1, padx=10, pady=5)

# Button Frame to contain buttons
btn_frame = tk.Frame(root)
btn_frame.grid(row=2, column=0, columnspan=2, pady=10)
# Buttons
tk.Button(btn_frame, text="Register", width=10, command=register).pack(side="left", padx=5)
tk.Button(btn_frame, text="Login", width=10, command=login).pack(side="left", padx=5)

# option 1
# # hyperlink forgot password
# forgot_label = tk.Label(root, text="Forgot Password?", fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
# forgot_label.grid(row=3, column=0, columnspan=2, pady=5)
# # bind click event
# forgot_label.bind("<Button-1>", forgot_password)

# --- Dictionary of hyperlinks ---
link_actions = {
    "Forgot Password?": forgot_password_action,
    "Help Center": help_action,
    "Contact Us": contact_action
}
# --- Add hyperlinks dynamically ---
row = 3
for text, action in link_actions.items():
    link = tk.Label(root, text=text, fg="blue", cursor="hand2", font=("Arial", 10, "underline"))
    link.grid(row=row, column=0, columnspan=2, pady=2)
    link.bind("<Button-1>", lambda e, act=action: act())
    row += 1

root.mainloop()
>>>>>>> f0961ba (Finish mini projects)
