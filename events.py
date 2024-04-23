from dotenv import load_dotenv
import os
import requests

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")


# given performer, get list of performer events
def get_events(event):
    # format event to be passed into url
    event = event.replace(" ", "-")
    url = 'https://api.seatgeek.com/2/events?performers.slug=' + event + '&client_id=' + CLIENT_ID

    try:
        response = requests.get(url)
        data = response.json()

        events_list = []
        for event in data['events']:
            event_id = event.get('id')
            datetime_utc = event.get('datetime_local')
            venue_name = event.get('venue', {}).get('name_v2')
            event_dict = {
                'id': event_id,
                'datetime_utc': datetime_utc,
                'venue_name_v2': venue_name,
            }
            events_list.append(event_dict)

        return events_list

    except Exception as e:
        print("Error:", e)
        return ()
