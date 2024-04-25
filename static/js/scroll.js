const homeButton = document.getElementById("home-button");
const homeButtonBlue = document.getElementById("home-button-blue");


function handleScroll() {
    const instructionsContainer = document.querySelector('.instructions-container');
    const linkButtons = document.querySelectorAll('#header-button, #login-button');
    const instructionsRect = instructionsContainer.getBoundingClientRect();

    // If header overlaps with instructions container rectangle
    if (instructionsRect.top <= 40) {
        linkButtons.forEach(button => {
            button.style.color = 'black';
            homeButton.style.display = "none";
            homeButtonBlue.style.display = "block";
        });
    } else {
        linkButtons.forEach(button => {
            button.style.color = 'white';
            homeButton.style.display = "block";
            homeButtonBlue.style.display = "none";
        });
    }
}


window.addEventListener('scroll', handleScroll);
