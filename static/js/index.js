function handleScroll() {
    const instructionsContainer = document.querySelector('.instructions-container');
    const linkButtons = document.querySelectorAll('#header-button, #login-button');
    const instructionsRect = instructionsContainer.getBoundingClientRect();

    // Check the positions of the container and adjust the colors accordingly
    if (instructionsRect.top <= 40) {
        linkButtons.forEach(button => {
            button.style.color = 'black';
        });
    } else {
        linkButtons.forEach(button => {
            button.style.color = 'white';
        });
    }
}

window.addEventListener('scroll', handleScroll);
