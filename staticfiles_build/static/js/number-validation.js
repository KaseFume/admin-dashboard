document.querySelector('.enter-button').addEventListener('click', function() {
    const prefix = document.getElementById('options').value;
    const number = document.getElementById('numberInput').value.trim();

    if (!number) {
        alert("Please enter a valid number.");
        return;
    }

    const productId = `${prefix}${number}`;

    fetch(`/check-product/${productId}/`)
        .then(response => response.json())
        .then(data => {
            if (data.exists) {
                window.location.href = `/update-form/${productId}/`;
            } else {
                window.location.href = `/add-form/${productId}/`;
            }
        })
        .catch(error => console.error('Error:', error));
});
