function initializeImageUploadPage() {
    const maxImages = 10;
    const imageUploadContainer = document.getElementById('imageUploadContainer');
    const addImageButton = document.getElementById('addImageButton');
    const numberInput = document.getElementById('numberInput'); // Assuming this is the ID of the input

    console.log('Number Validation is running');

    // Optional: Add validation to only allow numbers
    numberInput.addEventListener('input', function() {
        this.value = this.value.replace(/[^0-9]/g, ''); // Remove non-numeric characters
    });

    // Function to set up the file input change event listener
    function setupFileInput(fileInput, imagePreview) {
        fileInput.addEventListener('change', (event) => {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    imagePreview.src = e.target.result;
                    imagePreview.style.display = 'block';
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Set up the first image input
    const firstFileInput = document.querySelector('.image-input');
    const firstImagePreview = document.createElement('img');
    firstImagePreview.className = 'image-preview';
    firstImagePreview.style.display = 'none';
    firstImagePreview.style.maxWidth = '200px';
    firstImagePreview.style.marginTop = '10px';
    imageUploadContainer.appendChild(firstImagePreview);
    setupFileInput(firstFileInput, firstImagePreview);

    addImageButton.addEventListener('click', () => {
        const currentImages = document.querySelectorAll('.image-input').length;
        if (currentImages >= maxImages) {
            alert('You can only upload up to 10 images.');
            return;
        }

        const newInput = document.createElement('div');
        newInput.innerHTML = `
            <input type="file" name="images" class="image-input" accept="image/*">
            <button type="button" class="remove-button">Remove</button><br>
            <img class="image-preview" style="display:none; max-width: 200px; margin-top: 10px;" /><br><br>
        `;
        imageUploadContainer.appendChild(newInput);

        const fileInput = newInput.querySelector('.image-input');
        const imagePreview = newInput.querySelector('.image-preview');
        setupFileInput(fileInput, imagePreview);

        const removeButton = newInput.querySelector('.remove-button');
        removeButton.addEventListener('click', () => newInput.remove());
    });

    function setLastUpdatedTime() {
        const now = new Date();
        now.setMinutes(now.getMinutes() + (6 * 60) + 30); // Adjust to GMT+6:30
        const formattedDateTime = now.toISOString().slice(0, 19).replace('T', ' ');
        document.getElementById('lastUpdated').value = formattedDateTime;
    }

    setLastUpdatedTime();
}

window.initializeImageUploadPage = initializeImageUploadPage;
