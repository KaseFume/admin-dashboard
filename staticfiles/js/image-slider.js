console.log('Image-Slider is Running')
document.querySelectorAll('.image-slider').forEach((slider) => {
  const container = slider.querySelector('.slider-container');
  const images = container.querySelectorAll('img');
  const prevBtn = slider.querySelector('.prev-btn');
  const nextBtn = slider.querySelector('.next-btn');

  let currentIndex = 0;
  const totalImages = images.length;

  function updateSlider() {
      const offset = -currentIndex * 100;
      container.style.transform = `translateX(${offset}%)`;
  }

  prevBtn.addEventListener('click', () => {
      currentIndex = (currentIndex - 1 + totalImages) % totalImages;
      updateSlider();
  });

  nextBtn.addEventListener('click', () => {
      currentIndex = (currentIndex + 1) % totalImages;
      updateSlider();
  });

  // Optional: Add smooth transition
  container.style.transition = 'transform 0.5s ease-in-out';
});
