let currentIndex = 0;

function showImage(index) {
  const imageContainer = document.getElementById('image-container');
  const totalImages = imageContainer.children.length;

  // Ensure index stays within bounds
  if (index >= totalImages) currentIndex = 0;
  if (index < 0) currentIndex = totalImages - 1;

  // Slide to the correct image by adjusting the transform property
  imageContainer.style.transform = `translateX(-${currentIndex * 100}%)`;
}

function nextImage() {
  currentIndex++;
  showImage(currentIndex);
}

function prevImage() {
  currentIndex--;
  showImage(currentIndex);
}
