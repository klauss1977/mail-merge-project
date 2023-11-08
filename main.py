# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = []
with open("./Input/Names/invited_names.txt", mode="r") as name_file:
    names_raw = name_file.readlines()

for name in names_raw:
    names.append(name.strip())

with open("./Input/Letters/starting_letter.txt", mode="r") as text_file:
    letter_text = text_file.read()

for name in names:
    letter_to_send = letter_text.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as letter_file:
        letter_file.write(letter_to_send)
    print(letter_to_send)
