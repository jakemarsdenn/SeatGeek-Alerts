import re


# ensure email address is both valid and unique
def valid_account(name, email, password):
    if not valid_email(email):
        return "Invalid email address. Please try again."
    if not unique_email(email):
        return "An account with this email already exists."
    write_to_file(name, email, password)
    return "Sign up successful!"


# ensure email address is valid
def valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    return False


# ensure email address is unique
def unique_email(email):
    with open("users.txt", 'r') as file:
        for line in file:
            if f'Email: {email}' in line:
                return False
    return True


# write account credentials to txt file
def write_to_file(name, email, password):
    with open("users.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Password: {password}\n")


# check if email + password combination exists
def valid_credentials(email, password):
    with open("users.txt", 'r') as file:
        for line in file:
            if f'Email: {email}, Password: {password}' in line:
                return True
    return False

