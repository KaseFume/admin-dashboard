function initializeImageUploadPage(existingImages) {
    const maxImages = 10;
    const imageUploadContainer = document.getElementById('imageUploadContainer');
    const addImageButton = document.getElementById('addImageButton');
    let currentImagesCount = existingImages.length;

    function loadExistingImages(images) {
        images.forEach((imagePath, index) => {
            const imageWrapper = document.createElement('div');
            imageWrapper.className = 'image-wrapper';
            imageWrapper.innerHTML = `
                <img src="${imagePath}" class="image-preview" style="max-width: 200px; margin-top: 10px;" />
                <button type="button" class="replace-button" data-index="${index}">Replace</button>
                <button type="button" class="remove-button" data-index="${index}">Remove</button><br><br>
            `;
            imageUploadContainer.appendChild(imageWrapper);

            // Add remove functionality
            imageWrapper.querySelector('.remove-button').addEventListener('click', () => {
                imageWrapper.remove();
                currentImagesCount--;
                checkImageLimit();
            });

            // Add replace functionality
            imageWrapper.querySelector('.replace-button').addEventListener('click', () => {
                const fileInput = document.createElement('input');
                fileInput.type = 'file';
                fileInput.accept = 'image/*';
                fileInput.style.display = 'none';

                fileInput.addEventListener('change', (event) => {
                    const file = event.target.files[0];
                    if (file) {
                        const reader = new FileReader();
                        reader.onload = function (e) {
                            imageWrapper.querySelector('.image-preview').src = e.target.result;
                        };
                        reader.readAsDataURL(file);
                    }
                });
                fileInput.click();  // Trigger file input dialog
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

    // Load existing images if available
    if (existingImages.length > 0) {
        loadExistingImages(existingImages);
    } else {
        addInitialImageInput(); // Add initial input only if no existing images
    }

    addImageButton.addEventListener('click', handleNewImageUploads);
}

