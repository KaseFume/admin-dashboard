// Function to initialize the image upload functionality and set up event listeners
function initializeImageUploadPage() {
    const maxImages = 10;
    const imageUploadContainer = document.getElementById('imageUploadContainer');
    const addImageButton = document.getElementById('addImageButton');
    const numberInput = document.getElementById('numberInput');

    console.log('Number Validation is running');

    // Optional: Add validation to only allow numbers in the numberInput field
    numberInput.addEventListener('input', function() {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    // Function to set up the file input change event listener for previewing images
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

    // Initialize the first image input for preview
    const firstFileInput = document.querySelector('.image-input');
    const firstImagePreview = document.createElement('img');
    firstImagePreview.className = 'image-preview';
    firstImagePreview.style.display = 'none';
    firstImagePreview.style.maxWidth = '200px';
    firstImagePreview.style.marginTop = '10px';
    imageUploadContainer.appendChild(firstImagePreview);
    setupFileInput(firstFileInput, firstImagePreview);

    // Add more image upload fields when "Add Another Image" is clicked
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

    // Set initial value for the lastUpdated field to the current date and time
    function setLastUpdatedTime() {
        const now = new Date();
    
        // Calculate the offset in minutes for GMT+6:30
        const offset = 6 * 60 + 30; // 6 hours and 30 minutes
        const utcTime = now.getTime() + (now.getTimezoneOffset() * 60000); // Convert local time to UTC
        const gmt630Time = new Date(utcTime + (offset * 60000)); // Adjust to GMT+6:30
    
        // Format the date to "Nov. 3, 2024, 3:32 p.m."
        const options = { 
            year: 'numeric', 
            month: 'short', 
            day: 'numeric', 
            hour: 'numeric', 
            minute: 'numeric', 
            hour12: true 
        };
        const formattedDateTime = gmt630Time.toLocaleString('en-US', options).replace(',', ''); // Remove comma between date and time
    
        document.getElementById('lastUpdated').value = formattedDateTime; // Set the current time
    }

    setLastUpdatedTime();
}

// Immediate function call
initializeImageUploadPage();
