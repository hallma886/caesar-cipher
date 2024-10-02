alphabet = "abcdefghijklmnopqrstuvwxyz"
new_message = ""

user_message = input("Enter your secret message:\n")
key = int(input("Enter a key:\n"))
# print(user_message)

for character in user_message:
    if character in alphabet:
        psition = alphabet.find(character)
        new_position = (psition + key) % 26
        new_character = alphabet[new_position]
        new_message+= new_character
print("Your new message is " + new_message)
