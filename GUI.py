import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("600x450")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=15,padx=35,fill="both",expand=True)

user_entry =ctk.CTkEntry(master=frame,placeholder_text="username")
user_entry.pack(pady=12,padx=10)
password_entry = ctk.CTkEntry(master=frame,placeholder_text="password",show="*")
password_entry.pack(pady=12,padx=10)

button =ctk.CTkButton(master=frame, text=Login, width=120, height=32, border_width = 2)
button.pack(padx=0,pady=10)
root.mainloop()
