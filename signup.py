import re


def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)


def sign_up():
    name = input("Enter your name: ")

    while True:
        email = input("Enter your email address: ")

        if not validate_email(email):
            print("Invalid email address. Please try again.")
            continue

        with open("users.txt", "a") as file:
            file.write(f"Name: {name}, Email: {email}\n")

        print("Sign up successful!")
        break
