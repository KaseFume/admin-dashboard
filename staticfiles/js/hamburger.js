document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('hamburger');
    const sidebar = document.querySelector('.sidebar');
    
    hamburger.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed'); // Toggle the collapsed class
    });
});
