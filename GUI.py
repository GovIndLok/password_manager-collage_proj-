from customtkinter import *
import tkinter as tk
import login_module 
import encryption_module
import os
import csv
        

#root class for the main application
class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__() 

        # Create the main frame
        self.container = CTkFrame(self)
        self.container.pack(fill='both', expand=True)
        self.geometry("550x500")
        
        # Creating session object
        self.session = {}

        # Create the login frame
        self.login_frame = LoginFrame(self.container, session=self.session)
        self.login_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create the add user frame
        self.add_user_frame = AddUserFrame(self.container)
        self.add_user_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Creating password manger field
        
        #self.password_table_frame.pack_forget() 

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
        frame.destroy()
        self.password_table_frame = PasswordFrame(self.container, self.session['username'],self.session['passkey'])
        self.password_table_frame.pack(fill='both', expand = True)
        self.password_table_frame.place(relx = 0.0, rely = 0.0, anchor = "nw")
        self.password_table_frame.tkraise()
        

#login frame configration
class LoginFrame(CTkFrame):
    def __init__(self, parent, session):
        super().__init__(parent)
        
        self.session = session

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
        user = self.username_entry.get()
        password = self.password_entry.get()
        if login_module.user_login(user, password) == True:
            self.login_status_label.configure(text="login in successfully", text_color="green")
            
            self.session['username'] = user
            self.session['passkey'] = password
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
        self.back_button = CTkButton(self, text='Back', command=lambda: parent.master.show_frame('add_user','login'))
        self.back_button.pack(side='top', pady=5)
        
        #self.un = parent.master.UserName 
        #self.passw = parent.master.Master_Password
        self.parent = parent.master

    def adding_user(self):
        # Add the user
        username = self.username_entry.get()
        password = self.password_entry.get()
        if len(password) > 16:
            self.add_user_status_label.configure(text='password exceeded 16 chr length',text_color='red')
            return None
        else:
            if len(password) < 16:
                password = password.ljust(16, '\x00')
            login_module.add_user(username,password)
            self.un = username
            self.passw = password
            self.master.show_table('add_user')
            
class PasswordFrame(CTkFrame):
    def __init__(self, parent, usern, passk):
        super().__init__(parent)
        
        
        self.user =usern
        self.passkey = passk
        
        # Configuring the Grid
        self.grid_columnconfigure((0,1,2),weight=0)
        self.grid_rowconfigure((0,1,2),weight = 1)
        self.grid_rowconfigure(3, weight=3)
        
        #creating add password field
        self.add_password_frame = CTkFrame(self)
        self.add_password_frame.grid(row = 0,column=0,columnspan=3, rowspan=3)
        self.add_password_frame.grid_columnconfigure((0,2),weight=1)
        self.add_password_frame.grid_rowconfigure((0,1,2), weight=0)
        
        # Creating add password service field
        self.password_service_entry = CTkEntry(self.add_password_frame, placeholder_text="Service Name")
        self.password_service_entry.grid(row = 0, column= 0, padx=10,pady=10, sticky='nsew')
        
        #Creating add password field
        self.add_password_entry = CTkEntry(self.add_password_frame,placeholder_text="Set Password")
        self.add_password_entry.grid(row=1,column=0,padx=10,pady=10, sticky='nsew')
        
        # Creating Add new password button
        self.add_password_button = CTkButton(self.add_password_frame,text='Add\n Password',width=140, command=self.addpassword_fun)
        self.add_password_button.grid(row=2, column=0,columnspan=1, padx=5, pady=5, sticky = 'nsew')
        
        # Creating a add password label
        self.add_password_label = CTkLabel(self.add_password_frame, text='')
        self.add_password_label.grid(row=2, column=1,columnspan=1, padx=5, pady=5, sticky = 'nsew')
        
        # Creating Generate password button
        self.generate_password_button = CTkButton(self.add_password_frame, text='Create\n Password', command=self.generatepassword)
        self.generate_password_button.grid(row=2, column=2, padx=5, pady=5, sticky = 'nsew')
        
        # Creation of scrollable frame 
        self.scrollable_frame  = CTkScrollableFrame(self)
        self.scrollable_frame.grid(row =3,column=0, columnspan=3)#,rowspan=3)
        self.scrollable_frame.grid_columnconfigure((0,1),weight=1)
        self.scrollable_frame_button = []
        self.scrollable_frame_label = []
        self.password_filepath = f'data\\user_data\\{self.user}.csv'
        try:
            with open(self.password_filepath,mode='r',newline='') as csvfile: #getting a reader for the file
                read = csv.reader(csvfile)
                reader = list(read)
            # Showing the password list in the table
            for index, entry in enumerate(reader):
                # Showing Services in the list
                password_service_label = CTkLabel(self.scrollable_frame, text=entry[0])
                password_service_label.grid(row=index,column=0, padx=5, pady=5)
                self.scrollable_frame_label.append(password_service_label)
            
                # Showing the button
                password_copy_button = CTkButton(self.scrollable_frame,text='Copy',command=self.decrypt_copy)
                password_copy_button.grid(row=index,column=1,padx=5,pady=5)
                self.scrollable_frame_button.append(password_copy_button)
        except FileNotFoundError:
            self.table_empty_window = CTkLabel(self.scrollable_frame, text="No Saved Passwords", font=CTkFont(size=15, weight="bold"))
            self.table_empty_window.grid(row=1,column=1)
        
    def addpassword_fun(self):
        service = self.password_service_entry.get()
        password =self.add_password_entry.get()
        if len(password) > 32:
            self.add_password_label.configure(text="Password excced\n 32 caracters", text_color='red')
            return None
        else:
            encryption_module.encrypt_password(user=self.user,service=service,key=self.passkey,password=password)
            self.add_password_label.configure(text="Password added\n successfully", text_color='green')
            
    
    def generatepassword():
        t 
    
    def decrypt_copy():
        t 

# Create the PasswordManager instance
app = PasswordManager()

# Start the event loop
app.mainloop()
