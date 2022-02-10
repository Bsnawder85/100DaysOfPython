from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    text = my_input.get()
    my_label["text"] = text


my_label = Label(text="My first label.")
my_button = Button(text="Click Me", command=button_clicked)
new_button = Button(text="Click Me Too", command=button_clicked)
my_input = Entry(width=10)

my_label.grid(column=0, row=0)
my_button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
my_input.grid(column=3, row=2)

window.mainloop()

