async function navigateTo(page, sectionId = null) {
    const loadingIndicator = document.createElement('div');
    loadingIndicator.className = 'loading-indicator active';
    document.body.appendChild(loadingIndicator);

    try {
        const response = await fetch(`${page}.html`);
        if (response.ok) {
            const content = await response.text();
            document.getElementById('super-container').innerHTML = content;

            // Manually run any inline or external scripts inside the loaded content
            runPageScripts();

            // Initialize list pages if applicable
            if (['Ring_view', 'Earring_view', 'Pendant_view', 'Necklace_view', 'EPRset_view', 'Handchain_view'].includes(page)) {
                if (window.initializeListPage) {
                    window.initializeListPage(); // Call the function from script-list.js
                } else {
                    console.error('initializeListPage function not found.');
                }
            }

            // Initialize image upload page if applicable
            if (['form', 'add-form', 'update-form'].includes(page)) {
                if (window.initializeImageUploadPage) {
                    window.initializeImageUploadPage(); // Call the function from image upload JS file
                } else {
                    console.error('initializeImageUploadPage function not found.');
                }
            }

            // Scroll to the section if sectionId is provided
            if (sectionId) {
                const section = document.getElementById(sectionId);
                if (section) {
                    section.scrollIntoView({ behavior: 'smooth' });
                } else {
                    console.warn(`Section with ID '${sectionId}' not found.`);
                }
            }
        } else {
            document.getElementById('super-container').innerHTML = "<p>Page not found.</p>";
        }
    } catch (error) {
        console.error("Error loading page:", error);
        document.getElementById('super-container').innerHTML = "<p>Error loading the page.</p>";
    } finally {
        loadingIndicator.classList.remove('active');
        setTimeout(() => loadingIndicator.remove(), 300);
    }
}

function runPageScripts() {
    const scripts = document.querySelectorAll('#super-container script');
    scripts.forEach(oldScript => {
        const newScript = document.createElement('script');
        if (oldScript.src) {
            newScript.src = oldScript.src;
            newScript.async = false;
            newScript.onload = () => oldScript.remove();
        } else {
            newScript.textContent = oldScript.textContent;
        }
        document.body.appendChild(newScript);
    });
}

// Load the home page by default on page load
window.addEventListener('load', () => navigateTo('home'));
