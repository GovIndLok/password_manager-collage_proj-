from customtkinter import *
import tkinter as tk
import login_module 

class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the main frame
        self.container = CTkFrame(self)
        self.container.pack(fill='both', expand=True)

        # Create the login frame
        self.login_frame = LoginFrame(self.container)
        self.login_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create the add user frame
        self.add_user_frame = AddUserFrame(self.container)
        self.add_user_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Show the login frame
        self.show_frame('login')

    def show_frame(self, frame_name):
        # Raise the specified frame to the top
        frame = getattr(self, f'{frame_name}_frame')
        frame.tkraise()

class LoginFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create the username entry
        self.username_label = CTkLabel(self, text='Username:')
        self.username_label.pack(side='top', pady=5)
        self.username_entry = CTkEntry(self)
        self.username_entry.pack(side='top', pady=5)

        # Create the password entry
        self.password_label = CTkLabel(self, text='Password:')
        self.password_label.pack(side='top', pady=5)
        self.password_entry = CTkEntry(self, show='*')
        self.password_entry.pack(side='top', pady=5)

        # Create the login button
        self.login_button = CTkButton(self, text='Login', command=self.login)
        self.login_button.pack(side='top', pady=5)

        # Create the add user button
        self.add_user_button = CTkButton(self, text='Add User', command=lambda: parent.master.show_frame('add_user'))
        self.add_user_button.pack(side='top', pady=5)

    def login(self):
        # Check the username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
        # ...
        # Login logic here
        # ...

class AddUserFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create the username entry
        self.username_label = CTkLabel(self, text='New Username:')
        self.username_label.pack(side='top', pady=5)
        self.username_entry = CTkEntry(self)
        self.username_entry.pack(side='top', pady=5)

        # Create the password entry
        self.password_label = CTkLabel(self, text='New Password:')
        self.password_label.pack(side='top', pady=5)
        self.password_entry = CTkEntry(self, show='*')
        self.password_entry.pack(side='top', pady=5)

        # Create the add user button
        self.add_user_button = CTkButton(self, text='Add User', command=self.adding_user)
        self.add_user_button.pack(side='top', pady=5)
        
        #Create a add user label
        add_user_status_label = CTkLabel(self, text="")
        add_user_status_label.pack(side='top',pady=5)

        # Create the back button
        self.back_button = CTkButton(self, text='Back', command=lambda: parent.master.show_frame('login'))
        self.back_button.pack(side='top', pady=5)

    def adding_user(self):
        # Add the user
        username = self.username_entry.get()
        password = self.password_entry.get()
        if len(password) >= 16:
            add_user_status_label.configure(text='password exceeded 24 chr length')
            return None
        else:
            if len(password) < 16:
                password = password.ljust(16, '\x00')
            login_module.add_user(username,password)

# Create the PasswordManager instance
app = PasswordManager()

# Start the event loop
app.mainloop()
