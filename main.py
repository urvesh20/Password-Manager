from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    import random

    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for char in range(nr_letters)]
    password_list2 = [random.choice(symbols) for char in range(nr_symbols)]
    password_list3 = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # password = ""
    # for char in password_list:
    #     password += char


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_button_click():
    user_web_entry = website_entry.get()
    user_email_entry = email_entry.get()
    user_pass_entry = password_entry.get()
    new_data = {
        user_web_entry: {
            "email": user_email_entry,
            "password": user_pass_entry,

        }}

    if len(user_web_entry) == 0 or len(user_email_entry) == 0 or len(user_pass_entry) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")
    else:

        # is_ok = messagebox.askokcancel(title=user_web_entry,
        #                                message=f"These are the details entered: \nEmail: {user_email_entry} "
        #                                        f"\nPassword: {user_pass_entry} \nDo you want to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # Reading Old Data
                data = json.load(data_file)
                # Updating the old data with new data
                data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# Search password

def search():
    user_web_entry = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        email = data[user_web_entry]["email"]
        password = data[user_web_entry]["password"]
        messagebox.showinfo(title=user_web_entry, message=f"Email id: {email}\nPassword: {password}")
    except KeyError:
        messagebox.showinfo(title="Error", message=f"Password not found for {user_web_entry}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#112D4E")

canvas = Canvas(width=200, height=200, bg="#889EAF", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "urveshpatel@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=add_button_click)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()
