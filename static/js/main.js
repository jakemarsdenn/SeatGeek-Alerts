// NOT WORKING
const Dotenv = require('dotenv-webpack');

module.exports = {
    // Your other webpack configuration
    plugins: [
        new Dotenv()
    ]
};

const CLIENT_ID = process.env.CLIENT_ID;

// get events given performer
async function getEvents() {
    var url = 'https://api.seatgeek.com/2/events/' + 6037366 + '?client_id=' + CLIENT_ID;

    try {
        const response = await fetch(url);

        if (!response.ok) {
            console.error('Error fetching data:', response.statusText);
            return;
        }

        const data = await response.json();

        console.log(data);
    } catch (error) {
        console.error('Error:', error);
    }
}

getEvents()





