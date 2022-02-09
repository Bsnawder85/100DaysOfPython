# TODO 1. Create a dictionary in this format:
#  {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

nato_alpha_df = pandas.read_csv("nato_phonetic_alphabet.csv")

user_word = input("Enter a word: ").upper()

phonetics = [
    row.code for letter in user_word for (index, row) in nato_alpha_df.iterrows() if letter == row.letter
]
print(phonetics)
