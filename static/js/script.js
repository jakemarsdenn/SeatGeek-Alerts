require('dotenv').config();
const CLIENT_ID = process.env.CLIENT_ID;

// get events given performer
function getEvents(performer) {
    var axios = require('axios');
    var url = "https://api.seatgeek.com/2/events?performers.slug=" + performer + "&client_id=" + CLIENT_ID;

    return axios.get(url)
        .then(function(response) {
            var eventData = response.data;
            // Extract events with their IDs
            var eventsWithIds = eventData.events.map(function(event) {
                return {
                    id: event.id,
                    title: event.title,
                    datetime_utc: event.datetime_utc
                };
            });
            console.log(eventsWithIds);
            return JSON.stringify(eventsWithIds);
        })
        .catch(function(error) {
            console.error(error);
            return "[]";
        });
}

// getEvents("drake");

