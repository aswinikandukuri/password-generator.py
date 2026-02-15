import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return "No character type selected!"

    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("*** 🔒 Random Password Generator  🔒 ***")

length = int(input("Enter password length: "))

letters = input("Include letter's ? (y/n): ").lower() == "y"
numbers = input("Include number's ? (y/n): ").lower() == "y"
symbols = input("Include symbol's ? (y/n): ").lower() == "y"

password = generate_password(length, letters, numbers, symbols)
print("Generated Password 🔑 is:", password)
