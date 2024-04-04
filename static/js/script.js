require('dotenv').config();
const CLIENT_ID = process.env.CLIENT_ID;

function checkPrices() {
    const axios = require('axios');
    const performer = "drake"; // placeholder
    const url = "https://api.seatgeek.com/2/events?performers.slug=" + performer + "&client_id=" + CLIENT_ID;

    axios.get(url)
        .then(response => {
            const eventData = response.data;
            // Extract events with their IDs
            const eventsWithIds = eventData.events.map(event => ({
                id: event.id,
                title: event.title,
                datetime_utc: event.datetime_utc
            }));
            console.log(eventsWithIds);
        })
        .catch(error => {
            console.error(error);
        });
}

checkPrices();



