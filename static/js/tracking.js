const errorMsg = document.getElementById("error-message");


function validateInput(event) {
    const inputValue = document.getElementById('search-bar').value;
    const sixDigitIntRegex = /^\d{7}$/;
    // if event ID isn't a 7-digit integer
    if (!sixDigitIntRegex.test(inputValue)) {
        event.preventDefault();
        errorMsg.style.display = "block";
        return false;
    }
    return true;
}