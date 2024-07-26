import tkinter
import tkinter.messagebox
from password import get_password
import pyperclip
import json

#Search function
def search():
    try:
        with open("pass.json",'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    try:
        info = data[web_entry.get()]
    except KeyError as key:
        tkinter.messagebox.showwarning(message=f"No entry for website {key}, please check spelling")
    else:
        tkinter.messagebox.showinfo(message=f"Username: {info['user']}\n Password: {info['password']}")
    


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
    new_data = {
        web_entry.get(): {
            "user": user_entry.get(),
            "password": pass_entry.get()
            }}

    if web_entry.get() == "" or user_entry.get() == "" or pass_entry.get() == "":
        tkinter.messagebox.showwarning(title="Missing Field(s)",message="You didn't enter one or more fields")
    else:
        try:
            with open("pass.json","r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:        
            with open('pass.json','w') as file:
                json.dump(data,file,indent=4)
        
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

web_entry = tkinter.Entry(width=20)
web_entry.grid(column=1,row=1)
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

#Search button for v2
search_button = tkinter.Button(text="Search",command=search,width=15)
search_button.grid(column=2,row=1)






window.mainloop()



