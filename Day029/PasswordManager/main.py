from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=30)
# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
# Labels
website_label = Label(text="Website:")
email_username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
# Entries
website_entry = Entry(width=35)
email_username_entry = Entry(width=35)
password_entry = Entry(width=21)
# Buttons
generate_password_button = Button(text="Generate Password")
add_password_button = Button(text="Add", width=36)

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=2)
email_username_label.grid(row=2, column=0)
email_username_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_password_button.grid(row=3, column=2)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
