from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_label = Label(text="Miles")
equal_to_label = Label(text="is equal to")
output_label = Label(text="0")
km_label = Label(text="Km")
calculate_button = Button(text="Calculate")

miles_input.grid(row=0, column=1)
miles_label.grid(row=0, column=2)
equal_to_label.grid(row=1, column=0)
output_label.grid(row=1, column=1)
km_label.grid(row=1, column=2)
calculate_button.grid(row=2, column=1)

window.mainloop()
