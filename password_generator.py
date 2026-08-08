import random
again = "yes"
while again == "yes":
    letters_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    special_characters = "!@#$%^&*"

    length = int(input("Enter password length:"))
    special = input("include special characters? (yes/no):").lower()

    if special == "yes":
        characters = letters_numbers + special_characters
    else:
        characters = letters_numbers
    password =""
    for i in range(length):
        password += random.choice(characters)
    print("Generated password:", password)
    again = input("Generate another password? (yes/no):").lower()
print("Thank you for using the password generator!")    