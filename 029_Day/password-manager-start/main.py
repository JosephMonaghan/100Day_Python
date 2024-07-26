import tkinter
import tkinter.messagebox
import random
from password import get_password
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_password():
    password = get_password()

    pass_entry.delete(0,'end')
    pass_entry.insert(0,password)
    pyperclip.copy(password)






# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    pass_string = f"{web_entry.get()} | {user_entry.get()} | {pass_entry.get()} \n"

    if web_entry.get() == "" or user_entry.get() == "" or pass_entry.get() == "":
        is_ok = False
        tkinter.messagebox.showwarning(title="Missing Field(s)",message="You didn't enter one or more fields")
    else:
        message_txt =f"These are the details you entered:\nUser: {user_entry.get()}\nPassword: {pass_entry.get()}\n Is it ok to save?"
        is_ok=tkinter.messagebox.askokcancel(title=web_entry.get(),message=message_txt)
    
    if is_ok:
        with open("pass.txt","a") as file:
            file.write(pass_string)
        
        web_entry.delete(0,'end')
        pass_entry.delete(0,'end')
        
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

#Logo
canvas = tkinter.Canvas(width=200, height=200,highlightthickness=0)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=img)
canvas.grid(column=1,row=0)

#Create website label/entry and pack in grid
web_label = tkinter.Label(text="Website:")
web_label.grid(column=0,row=1)

web_entry = tkinter.Entry(width=35)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()

#Create username/email entry and pack in grid
user_label = tkinter.Label(text="Email/Username:")
user_label.grid(column=0,row=2)

user_entry = tkinter.Entry(width=35)
user_entry.grid(column=1,row=2,columnspan=2)
user_entry.insert(0,"Joseph_Monaghan@outlook.com")

#Create password entry and pack in grid
pass_label = tkinter.Label(text="Password:")
pass_label.grid(column=0,row=3)

pass_entry = tkinter.Entry(width=21)
pass_entry.grid(column=1,row=3)

#Create generate password and save button and pack in grid
gen_pass = tkinter.Button(text="Generate Password",command=gen_password)
gen_pass.grid(column=2,row=3)

save_button = tkinter.Button(text="Add",width=36,command=save_pass)
save_button.grid(column=1,row=4,columnspan=2)






window.mainloop()



