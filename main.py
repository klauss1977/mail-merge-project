PLACEHOLDER = "[name]"
names = []
with open("./Input/Names/invited_names.txt") as names_file:
    names_raw = names_file.readlines()

for name in names_raw:
    names.append(name.strip())

with open("./Input/Letters/starting_letter.txt") as text_file:
    letter_text = text_file.read()

for name in names:
    letter_to_send = letter_text.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as letter_file:
        letter_file.write(letter_to_send)
    print(letter_to_send)
