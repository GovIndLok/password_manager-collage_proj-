import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")
# 
# root = ctk.CTk()
# root.title("password manager")
# root.geometry("600x450")

# frame = ctk.CTkFrame(master=root)
# frame.pack(pady=15,padx=35,fill="both",expand=True)

# user_entry =ctk.CTkEntry(master=frame,placeholder_text="username")
# user_entry.pack(pady=2,padx=10)
# password_entry = ctk.CTkEntry(master=frame,placeholder_text="password",show="*")
# password_entry.pack(pady=2,padx=10)

# button =ctk.CTkButton(master=frame, text="Login", width=120, height=32, command=frame_exit())
# button.pack(pady=2,padx=10)
# root.mainloop()

def validate_login(username, password):
    # Check if the username and password are valid
    # (e.g. by looking up the credentials in a database)
    if username == "user" and password == "password":
        return True
    else:
        return False

def login():
    username = username_entry.get()
    password = password_entry.get()

    if validate_login(username, password):
        login_status_label.config(text="Login successful!", fg="green")
    else:
        login_status_label.config(text="Invalid username or password", fg="red")

root = ctk.CTk()
root.title("Login Page")
root.geometry("600x450")

# Create the username label and entry
username_label = ctk.CTkLabel(root, text="Username")
username_label.pack()
username_entry = ctk.CTkEntry(root)
username_entry.pack()

# Create the password label and entry
password_label = ctk.CTkLabel(root, text="Password")
password_label.pack()
password_entry = ctk.CTkEntry(root, show="*")
password_entry.pack()

# Create the login button
login_button = ctk.CTkButton(root, text="Login", command=login)
login_button.pack()

# Create the login status label
login_status_label = ctk.CTkLabel(root, text="")
login_status_label.pack()

root.mainloop()