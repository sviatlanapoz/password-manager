from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbol = [choice(symbols) for char in range(randint(2, 4))]
    password_numb = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_numb
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_text = web_entry.get()
    email_text = email_entry.get()
    pass_text = pass_entry.get()
    new_data = {
        web_text: {
            "email": email_text,
            "password": pass_text,
        }
    }

    if len(web_text) == 0 or len(pass_text) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as f:
                # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(new_data, f, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)

        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- Find Password ----------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data_from_file = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data_from_file:
            email = data_from_file[website]["email"]
            password = data_from_file[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "user@mail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)










window.mainloop()
