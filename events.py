from dotenv import load_dotenv
import os
import requests


load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")


# EVENT MUST BE PASSED IN THE FORMAT name-name eg. bruno-mars

def get_events(event):
    url = 'https://api.seatgeek.com/2/events?performers.slug=' + event + '&client_id=' + CLIENT_ID

    try:
        response = requests.get(url)
        data = response.json()

        events_list = []
        for event in data['events']:
            event_type = event.get('type')
            event_id = event.get('id')
            datetime_utc = event.get('datetime_utc')
            venue_name = event.get('venue', {}).get('name_v2')
            event_dict = {
                'type': event_type,
                'id': event_id,
                'datetime_utc': datetime_utc,
                'venue_name_v2': venue_name,
            }
            events_list.append(event_dict)

        print(events_list)

    except Exception as e:
        print("Error:", e)


get_events("bruno-mars")



# curl 'https://api.seatgeek.com/2/events?performers.slug=new-york-mets&client_id=Mzk5NDU4MzZ8MTcwOTI1NTI3MS42ODg4NzEx'