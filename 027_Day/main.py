import tkinter


def calculate():
    miles_val = float(miles_entry.get())
    in_km = round(miles_val * 1.609,1)
    km_val["text"] = f"{in_km}"

window = tkinter.Tk()
window.title("Miles to km converter")
#window.minsize(width=350,height=200)
window.config(padx = 20,pady = 20)


miles_entry = tkinter.Entry(textvariable="0",width=4)
miles_entry.grid(column = 1, row = 0)

miles_label = tkinter.Label(text = "miles")
miles_label.grid(column=2,row=0)

km_leading_str = tkinter.Label(text = "is equal to")
km_leading_str.grid(column=0,row=1)

km_val = tkinter.Label(text= "0")
km_val.grid(column=1,row=1)

km_units =tkinter.Label(text="km")
km_units.grid(column=2,row=1)

calculate_button = tkinter.Button(text='Calculate',command=calculate)
calculate_button.grid(column=1,row=2)


window.mainloop()
