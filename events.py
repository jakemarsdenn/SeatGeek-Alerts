from dotenv import load_dotenv
import os
import requests


load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")


def getEvents():
    eventID = 6471282  # placeholder
    url = 'https://api.seatgeek.com/2/events/' + str(eventID) + '?client_id=' + CLIENT_ID

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

    except Exception as e:
        print("Error:", e)


# getEvents()