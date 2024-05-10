const errorMsg = document.getElementById("error-message");

function validateInput(event) {
    const inputValue = document.getElementById('search-bar').value;
    const sixDigitIntRegex = /^\d{7}$/;
    // If event ID isn't a 7-digit integer
    if (!sixDigitIntRegex.test(inputValue)) {
        event.preventDefault();
        errorMsg.style.display = "block";
        return false;
    }
    return true;
}


const form = document.getElementById('code-form');
const codeInputs = document.querySelectorAll('.code-input');

codeInputs.forEach((input, index) => {
    input.addEventListener('input', (event) => {
        const maxLength = parseInt(event.target.getAttribute('maxlength'));

        // Move to the next input field if a digit is entered
        if (event.target.value.length === maxLength) {
            if (index < codeInputs.length - 1) {
                codeInputs[index + 1].focus();
            } else {
                // Automatically submit the form after the 7th digit
                form.submit();
            }
        }
    });

    input.addEventListener('keydown', (event) => {
        if (event.key === 'Backspace' && input.value.length === 0) {
            if (index > 0) {
                codeInputs[index - 1].focus();
            }
        }
    });
});