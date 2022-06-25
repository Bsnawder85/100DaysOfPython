from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ==================== DATA ====================
vocabulary_csv = pandas.read_csv("data/french_words.csv")
vocab_data = pandas.DataFrame(data=vocabulary_csv, columns=["French", "English"]).to_dict(orient="records")
# ==================== LOGIC ====================
# TODO:
#  Pick a random French word/translation and put the word into the flashcard.
#  Every time you press the right or wrong buttons, it should generate a new random word to display.

# ==================== GUI ====================
# WINDOW
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# IMAGES
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
# FLASH CARD
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), justify="center")
canvas.create_text(400, 263, text="Some French vocab", font=("Arial", 60, "bold"), justify="center")
# BUTTONS
right_button = Button(image=right_image, highlightthickness=0)
wrong_button = Button(image=wrong_image, highlightthickness=0)
# PLACE ELEMENTS IN THE 2x2 GRID
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

window.mainloop()
