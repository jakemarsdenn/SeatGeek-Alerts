from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")


# given performer, get list of performer events
def get_events(performer):
    # format event to be passed into url
    performer = performer.replace(" ", "-")
    url = 'https://api.seatgeek.com/2/events?performers.slug=' + performer + '&client_id=' + CLIENT_ID

    try:
        response = requests.get(url)
        data = response.json()

        events_list = []
        for performer in data['events']:
            event_id = performer.get('id')
            datetime_utc = performer.get('datetime_local')
            venue_name = performer.get('venue', {}).get('name_v2')
            event_dict = {
                'id': event_id,
                'datetime': reformat_datetime(datetime_utc),
                'venue': venue_name,
            }
            events_list.append(event_dict)

        return events_list

    except Exception as e:
        print("Error:", e)
        return ()


def reformat_datetime(datetime_utc):
    date_time = datetime.strptime(datetime_utc, '%Y-%m-%dT%H:%M:%S')
    formatted_date_time = date_time.strftime('%A %-d %B, %-I%p')
    formatted_date_time = formatted_date_time.replace('AM', 'am').replace('PM', 'pm')
    return formatted_date_time


# given event ID, get event
def get_event(eventID):
    eventID = str(eventID)
    url = 'https://api.seatgeek.com/2/events/' + eventID + '?client_id=' + CLIENT_ID

    try:
        response = requests.get(url)
        data = response.json()

        event_id = data.get('id')
        performer = data['performers'][0]['name']
        datetime_utc = data.get('datetime_local')
        venue_name = data.get('venue', {}).get('name_v2')

        event_dict = {
            'id': event_id,
            'performer': performer,
            'datetime': reformat_datetime(datetime_utc),
            'venue': venue_name,
        }

        return event_dict

    except Exception as e:
        print("Error:", e)
        return ()
