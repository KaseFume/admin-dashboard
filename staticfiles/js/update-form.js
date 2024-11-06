function initializeImageUploadPage(existingImages) {
    const maxImages = 10;
    const imageUploadContainer = document.getElementById('imageUploadContainer');
    const addImageButton = document.getElementById('addImageButton');
    let currentImagesCount = existingImages.length;
    let imagesToRemove = []; // Array to store image paths to delete

    function loadExistingImages(images) {
        images.forEach((imagePath, index) => {
            const imageWrapper = document.createElement('div');
            imageWrapper.className = 'image-wrapper';
            imageWrapper.innerHTML = `
                <img src="${imagePath}" class="image-preview" style="max-width: 200px; margin-top: 10px;" />
                <input type="hidden" name="existing_image_paths" value="${imagePath}"> <!-- Track the image path -->
                <button type="button" class="remove-button" data-path="${imagePath}">Remove</button><br><br>
            `;
            imageUploadContainer.appendChild(imageWrapper);

            // Add remove functionality
            imageWrapper.querySelector('.remove-button').addEventListener('click', () => {
                imagesToRemove.push(imagePath); // Add image path to deletion list
                imageWrapper.remove(); // Remove the HTML element
                currentImagesCount--;
                checkImageLimit();
            });
        });
    }

    function addInitialImageInput() {
        const newInput = document.createElement('div');
        newInput.className = 'image-wrapper';
        newInput.innerHTML = `
            <input type="file" name="images" class="image-input" accept="image/*">
            <button type="button" class="remove-button">Remove</button><br>
            <img class="image-preview" style="display:none; max-width: 200px; margin-top: 10px;" /><br><br>
        `;
        imageUploadContainer.appendChild(newInput);

        const fileInput = newInput.querySelector('.image-input');
        const imagePreview = newInput.querySelector('.image-preview');
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

        newInput.querySelector('.remove-button').addEventListener('click', () => {
            newInput.remove();
            currentImagesCount--;
            checkImageLimit();
        });

        currentImagesCount++;
        checkImageLimit();
    }

    function handleNewImageUploads() {
        if (currentImagesCount >= maxImages) {
            alert('You can only upload up to 10 images.');
            return;
        }
        addInitialImageInput();
    }

    function checkImageLimit() {
        addImageButton.disabled = currentImagesCount >= maxImages;
    }

    // Add hidden field to store imagesToRemove array on form submission
    function addImagesToRemoveField() {
        const removeInput = document.createElement('input');
        removeInput.type = 'hidden';
        removeInput.name = 'images_to_remove_paths';
        removeInput.value = JSON.stringify(imagesToRemove); // Convert array to JSON string
        imageUploadContainer.appendChild(removeInput);
    }

    // Load existing images if available
    if (existingImages.length > 0) {
        loadExistingImages(existingImages);
    } else {
        addInitialImageInput(); // Add initial input only if no existing images
    }

    addImageButton.addEventListener('click', handleNewImageUploads);
    document.querySelector('form').addEventListener('submit', addImagesToRemoveField); // Add hidden field on submit
}
