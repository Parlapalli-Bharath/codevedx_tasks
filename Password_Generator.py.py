import random
import string

# Password Generator
def generate_password(length):
    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Password Strength Checker
def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score == 5:
        return "Very Strong 💪"
    elif score == 4:
        return "Strong 👍"
    elif score == 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"


# Main Menu
while True:
    print("\n===== PASSWORD GENERATOR & STRENGTH CHECKER =====")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            length = int(input("Enter password length: "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                password = generate_password(length)
                print("\nGenerated Password:", password)
                print("Strength:", check_strength(password))
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        password = input("Enter password to check: ")
        print("Password Strength:", check_strength(password))

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")