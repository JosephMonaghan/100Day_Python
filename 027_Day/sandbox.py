import tkinter


def button_listener():
    my_label["text"] = input.get()

window = tkinter.Tk()


window.title("My first python GUI")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

my_label = tkinter.Label(text="I am a label",font=("HELVETICA", 24, "bold"))
my_label.grid(column=0,row=0)
my_label.config(padx=100)


button = tkinter.Button(text="Update Label:",command=button_listener)
button.grid(column=1,row=1)

button2 = tkinter.Button(text="Button2")
button2.grid(column=2,row=0)

input = tkinter.Entry()
input.grid(column = 3, row = 2)


window.mainloop()


# numbers = [1,4,7,10]

# def add_all(*args):
#     total = 0
#     for num in args[0]:
#         total += num
    
#     return total


# print(add_all(numbers))