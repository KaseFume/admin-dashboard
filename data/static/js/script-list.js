// script-list.js

// Function to initialize dropdown and truncate logic
function initializeListPage() {
    console.log('Script LISTTT IS RUNNING');

    const container = document.querySelector('.list-container');
    if (!container) return;

    // Dropdown logic
    container.querySelectorAll('.dropdown-btn').forEach(btn => {
        btn.addEventListener('click', function (event) {
            event.stopPropagation();
            const dropdown = this.closest('.dropdown');
            dropdown.classList.toggle('show');

            // Close other dropdowns
            container.querySelectorAll('.dropdown').forEach(otherDropdown => {
                if (otherDropdown !== dropdown) {
                    otherDropdown.classList.remove('show');
                }
            });
        });
    });

    // Close dropdowns on outside click
    window.addEventListener('click', (e) => {
        if (!e.target.closest('.list-container .dropdown')) {
            container.querySelectorAll('.dropdown').forEach(dropdown => {
                dropdown.classList.remove('show');
            });
        }
    });

    // Close dropdown when clicking on an <li>
    container.querySelectorAll('.dropdown li').forEach(item => {
        item.addEventListener('click', (event) => {
            const dropdown = event.target.closest('.dropdown');
            if (dropdown) {
                dropdown.classList.remove('show');
            }
        });
    });

    // Call text truncation logic
    truncateText();
}

// Text truncation logic scoped to .list-container
function truncateText() {
    const container = document.querySelector('.list-container');
    if (!container) return;

    container.querySelectorAll('.truncate').forEach(cell => {
        const originalText = cell.innerText;
        const wordLength = originalText.replace(/[^a-zA-Z]/g, '').length;

        if (wordLength > 18) {
            const words = originalText.split(' ');
            let truncatedText = '';
            let lengthCount = 0;

            for (const word of words) {
                const cleanWord = word.replace(/[^a-zA-Z]/g, '');
                if (lengthCount + cleanWord.length > 18) break;
                truncatedText += word + ' ';
                lengthCount += cleanWord.length;
            }

            cell.innerText = truncatedText.trim() + '...';
        }
    });
}

// Expose initializeListPage to be used in other scripts
window.initializeListPage = initializeListPage;
