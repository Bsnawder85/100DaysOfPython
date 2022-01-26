# TODO: Create a letter using starting_letter.txt
#  for each name in invited_names.txt
#  Replace the [name] placeholder with the actual name.
#  Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#   Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#       Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as read_letter:
    letter = read_letter.read()

for name in names:
    stripped_name = name.strip()
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as write_file:
        new_letter = letter.replace("[name]", stripped_name)
        write_file.write(new_letter)
