// NOT WORKING
// require('dotenv').config();
// const CLIENT_ID = process.env.CLIENT_ID;

// get events given performer
async function getEvents() {
    var url = 'https://api.seatgeek.com/2/events/' + 6037366 + '?client_id=' + 'Mzk5NDU4MzZ8MTcwOTI1NTI3MS42ODg4NzEx';

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





