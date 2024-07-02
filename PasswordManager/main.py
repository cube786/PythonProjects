from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbols + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = username_entry.get()
    password = pass_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please dont leave any fields empty! ")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\nare you sure to save?")

        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)



website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "cube@gmail.com")
pass_entry = Entry(width=20)
pass_entry.grid(row=3, column=1)

gen_button = Button(text="Generate Password", command=generate)
gen_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()