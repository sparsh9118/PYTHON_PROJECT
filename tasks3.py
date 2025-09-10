import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":   # ✅ Corrected here
    print("Password Generator - Task 3")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 for better security.")
        else:
            password = generate_password(length)
            print("\nGenerated Password:", password)
    except ValueError:
        print("Please enter a valid number.")
