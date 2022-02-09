# TODO 1. Create a dictionary in this format:
#  {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

nato_alpha_df = pandas.read_csv("nato_phonetic_alphabet.csv")

print(nato_alpha_df)
