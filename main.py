from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo("Opps", "Don't leave any empty fields")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -----------------------------Search Password ---------------------------#

def find_password():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

            if website_data in data:
                email = data[website_data]["email"]
                password = data[website_data]["password"]
                messagebox.showinfo("Here are the deets", f"Twitter: {website_data}\nPassword: {password}")

            else:
                messagebox.showinfo("FYI","No details for website exists." )
    except FileNotFoundError:
        messagebox.showerror("Whoops","There is no file")


# # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white", highlightthickness=0)

canvas = Canvas(width=200, height=200, bg="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:", font=("Helvatica", 14), bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", font=("Helvatica", 14), bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=("Helvetica", 14), bg="white")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "youremail@whatever.com")
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="Generate Password",width=17, font="Helvetica", bg="white", command=generate_password)
generate_password_button.grid(row=3, column=2)
add = Button(text="Add", width=36, font="Helvetica", bg="white", command=save)
add.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", font="Helvetica", width=17, bg="White", command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
