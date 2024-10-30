// Function to calculate total purchased items
function calculateTotalPurchased() {
    const purchasedItems = document.querySelectorAll('.metric span.session-count');
    let totalPurchased = 0;

    purchasedItems.forEach(item => {
        const quantity = parseInt(item.textContent) || 0; // Get the value or default to 0
        totalPurchased += quantity; // Sum the quantities
    });

    // Update the total purchased element
    const totalPurchasedElement = document.querySelector('.metric:last-child span.session-count');
    totalPurchasedElement.textContent = totalPurchased; // Display the total
}

// Call the function to calculate total on page load or whenever needed
calculateTotalPurchased();
