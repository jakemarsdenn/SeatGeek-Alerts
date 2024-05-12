import re
import json


# Ensure email address is both valid and unique
def valid_account(name, email, password):
    if not valid_email(email):
        print("Invalid email address. Please try again.")
        return False
    if not unique_email(email):
        print("An account with this email already exists.")
        return False
    write_to_file(name, email, password)
    print("Sign up successful!")
    return True


# Ensure email address is valid
def valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    return False


# Ensure email address is unique
def unique_email(email):
    with open("users.json", 'r') as file:
        users = json.load(file)
        for user in users:
            if user['Email'] == email:
                return False
    return True


# Check if email + password combination exists
def valid_credentials(email, password):
    with open("users.json", 'r') as file:
        users = json.load(file)
        for user in users:
            if user['Email'] == email and user['Password'] == password:
                return True
    return False


# Write account credentials to JSON file
def write_to_file(name, email, password):
    new_user = {"Name": name, "Email": email, "Password": password}
    with open("users.json", "r+") as file:
        data = json.load(file)
        data.append(new_user)
        file.seek(0)
        json.dump(data, file, indent=4)


# Given user's email, find their name
def get_name(email):
    with open("users.json", 'r') as file:
        users = json.load(file)
        for user in users:
            if user['Email'] == email:
                return user['Name']


# Given user's email, find their tracked events
def get_tracked_events(email):
    with open("saved-events.json", 'r') as file:
        users = json.load(file)
        for user in users:
            if user['Email'] == email:
                return user['Saved_events']


# Change user's name
def edit_name(new_name, email):
    with open('users.json', 'r') as file:
        users = json.load(file)
        for user in users:
            if user['Email'] == email:
                user['Name'] = new_name
                break
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)


# Change user's password
def edit_password(new_password, email):
    with open('users.json', 'r') as file:
        users = json.load(file)
        for user in users:
            if user['Email'] == email:
                user['Password'] = new_password
                break
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)



