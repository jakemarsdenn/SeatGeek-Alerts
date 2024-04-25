document.addEventListener('DOMContentLoaded', function() {
    const scrollToTopLink = document.querySelector('.scroll-to-top-link');
    scrollToTopLink.addEventListener('click', function(event) {
        event.preventDefault();
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});