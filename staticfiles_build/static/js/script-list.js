document.addEventListener("DOMContentLoaded", function () {
    console.log("List page script initialized");

    // Dropdown Logic
    const dropdownButtons = document.querySelectorAll(".dropdown-btn");

    dropdownButtons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.stopPropagation(); // Prevent event from bubbling up to document

            const dropdownContainer = this.parentElement; // Get the parent dropdown container
            dropdownContainer.classList.toggle("show"); // Toggle 'show' on the entire dropdown container

            // Close other dropdowns
            document.querySelectorAll(".dropdown").forEach(dropdown => {
                if (dropdown !== dropdownContainer) {
                    dropdown.classList.remove("show"); // Remove 'show' class from other dropdowns
                    console.log('Other dropdown closed');
                }
            });
        });
    });

    // Close dropdowns on outside click
    document.addEventListener("click", function (event) {
        if (!event.target.closest(".dropdown")) {
            document.querySelectorAll(".dropdown").forEach(dropdown => {
                dropdown.classList.remove("show"); // Hide all dropdowns
                console.log('Dropdown menu closed on outside click');
            });
        }
    });

    // Text Truncation Logic
    const truncateElements = document.querySelectorAll(".truncate");
    truncateElements.forEach(cell => {
        const originalText = cell.innerText;
        const maxLength = 18;

        if (originalText.length > maxLength) {
            cell.innerText = originalText.slice(0, maxLength) + "..."; // Truncate text
        }
    });
});
