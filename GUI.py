from customtkinter import *
import tkinter as tk
import login_module 

#root class for the main application
class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the main frame
        self.container = CTkFrame(self)
        self.container.pack(fill='both', expand=True)
        self.geometry("550x500")
        

        # Create the login frame
        self.login_frame = LoginFrame(self.container)
        self.login_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create the add user frame
        self.add_user_frame = AddUserFrame(self.container)
        self.add_user_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Show the login frame
        self.show_frame('add_user','login')

    def show_frame(self,hidd_frame, frame_name):
        #hidding the current frame
        h_frame = getattr(self, f'{hidd_frame}_frame')
        h_frame.pack_forget()
        # Raise the specified frame to the top
        frame = getattr(self, f'{frame_name}_frame')
        frame.tkraise()
    
    def show_table(self, frame_name):
        frame = getattr(self, f'{frame_name}_frame')
        frame.master.pack_forget()
        
        #Create a scrollable frame
        #Create main frame
        self.scrollable = CTkScrollableFrame(self)
        self.scrollable.pack(fill='both', expand = True)
        self.password_table_frame = passwordFrame(self.scrollable)
        self.password_table_frame.pack(fill='both', expand=True)

#login frame configration
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
        self.add_user_button = CTkButton(self, text='Add User', command=lambda: parent.master.show_frame('login','add_user'))
        self.add_user_button.pack(side='top', pady=5)
        
        #Create a login status label
        self.login_status_label = CTkLabel(self, text="")
        self.login_status_label.pack(side='top',pady=5)
        
        self.table_screen = parent.master

    def login(self):
        # Check the username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
        if login_module.user_login(username, password) == True:
            self.login_status_label.configure(text="login in successfully", text_color="green")
            self.username = username
            self.master_password = password
            self.table_screen.show_table('login')
        else:
            self.login_status_label.configure(text="login in unsuccessfully", text_color="red")

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
        self.add_user_status_label = CTkLabel(self, text="")
        self.add_user_status_label.pack(side='top',pady=5)

        # Create the back button
        self.back_button = CTkButton(self, text='Back', command=lambda: parent.master.show_frame('login'))
        self.back_button.pack(side='top', pady=5)

    def adding_user(self):
        # Add the user
        username = self.username_entry.get()
        password = self.password_entry.get()
        if len(password) >= 16:
            self.add_user_status_label.configure(text='password exceeded 24 chr length',text_color='red')
            return None
        else:
            if len(password) < 16:
                password = password.ljust(16, '\x00')
            login_module.add_user(username,password)
            self.master.show_table('add_user')
            
class passwordFrame(CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        

# Create the PasswordManager instance
app = PasswordManager()

# Start the event loop
app.mainloop()
