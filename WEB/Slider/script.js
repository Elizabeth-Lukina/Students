const slides = [
    "img/1.jpg",
    "img/2.jpg",
    "img/3.jpg",
    "img/4.jpg",
    "img/5.jpg"
];

let currentSlideIndex = 0;
const totalSlides = slides.length;

const slideImage = document.getElementById('slide');
const counterDisplay = document.getElementById('counter');

function updateSlider() {
    slideImage.src = slides[currentSlideIndex];
    counterDisplay.textContent = `Изображение ${currentSlideIndex + 1} из ${totalSlides}`;
}

document.getElementById('next').addEventListener('click', () => {
    currentSlideIndex = (currentSlideIndex + 1) % totalSlides; // зацикливание
    updateSlider();
});

document.getElementById('prev').addEventListener('click', () => {
    currentSlideIndex = (currentSlideIndex - 1 + totalSlides) % totalSlides; // зацикливание
    updateSlider();
});

// Инициализация слайдера
updateSlider();