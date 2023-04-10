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
        login_status_label.configure(text="Login successful!", fg="green")
    else:
        login_status_label.configure(text="Invalid username or password", fg="red")

root = ctk.CTk()
root.title("Login Page")
root.geometry("450x450")

def add_user():
    # Code to add a new user
    pass

# Create the add user button
add_user_button = ctk.CTkButton(root, text="+", command=add_user, width=15,height=15)
add_user_button.pack(side=ctk.LEFT,padx=5)


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
login_button.pack(pady= 10, padx=10)

# Create the login status label
login_status_label = ctk.CTkLabel(root, text="")
login_status_label.pack()

root.mainloop()