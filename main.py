import json
import os

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# # Load OAuth credentials
# credentials = Credentials.from_authorized_user_file('/Users/JakeMarsden/Desktop/credentials.json')
#
# # Authorize the credentials
# if credentials.expired and credentials.refresh_token:
#     credentials.refresh(Request())
#
# # Extract script ID from credentials.json
# with open('credentials.json') as f:
#     credentials_data = json.load(f)
#     script_id = credentials_data['installed']['project_id']
#
# # Build the Google Apps Script API service
# service = build('script', 'v1', credentials=credentials)
#
#
# # Define the function to execute the script
# def run_script(script_id, function_name):
#     # Call the Apps Script API
#     request = service.scripts().run(body={
#         "function": function_name,
#         "scriptId": script_id
#     })
#     response = request.execute()
#     return response
#
#
# # Example usage
# if __name__ == "__main__":
#     function_name = "FUNCTION_NAME"
#     response = run_script(script_id, function_name)
#     print(response)


def track_event(event_id, email):
    filename = 'saved-events.json'
    try:
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
        else:
            data = []
    except json.decoder.JSONDecodeError:
        data = []

    found = False
    for user in data:
        if user['Email'] == email:
            if event_id in user['Saved_events']:
                print("You have already saved this event")  # DISPLAY TO USER
            else:
                user['Saved_events'].append(event_id)
            found = True
            break

    if not found:
        data.append({'Email': email, 'Saved_events': [event_id]})

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def untrack_event(event_id, email):
    filename = 'saved-events.json'
    try:
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
        else:
            return
    except json.decoder.JSONDecodeError:
        print("Error decoding JSON data.")
        return

    for user in data:
        if user['Email'] == email:
            if event_id in user['Saved_events']:
                user['Saved_events'].remove(event_id)
                break

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
