console.log('Image-Slider is Running');

document.querySelectorAll('.image-slider').forEach((slider) => {
    const container = slider.querySelector('.slider-container');
    const images = container.querySelectorAll('img');
    const prevBtn = slider.querySelector('.prev-btn');
    const nextBtn = slider.querySelector('.next-btn');

    let currentIndex = 0;
    const totalImages = images.length;

    function updateSlider() {
        const offset = -currentIndex * 100; // Each image takes up 100% of the width
        container.style.transform = `translateX(${offset}%)`;
    }

    prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + totalImages) % totalImages; // Wrap around
        updateSlider();
    });

    nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % totalImages; // Wrap around
        updateSlider();
    });

    // Optional: Initialize the slider position
    updateSlider();
});
