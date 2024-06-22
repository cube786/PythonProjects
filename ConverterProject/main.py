from tkinter import *

window = Tk()
window.minsize(width=500, height=250)
window.title("Mile to Km Converter")
window.config(padx=100, pady=100)


def miles_to_kilometers():
    miles = float(entry.get())
    # mile_to_int = int(miles)
    km = miles * 1.609
    label3.config(text=f"{km}")


entry = Entry(width=30)
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = Label(text=0)
label3.grid(column=1, row=1)
label4 = Label(text="Km")
label4.grid(column=2, row=1)
button = Button(text="Calculate", width=25, command=miles_to_kilometers)
button.grid(column=1, row=2)
window.mainloop()