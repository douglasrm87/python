// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    
    // ... (código existente da tela de pedidos e relatórios) ...

    // --- LÓGICA DO CARROSSEL DA HOMEPAGE ---
    const carouselWrapper = document.querySelector('.carousel-wrapper');
    if (carouselWrapper) {
        const slides = document.querySelectorAll('.carousel-slide');
        const prevBtn = document.querySelector('.carousel-control.prev');
        const nextBtn = document.querySelector('.carousel-control.next');
        const dotsContainer = document.querySelector('.carousel-dots');
        let currentIndex = 0;
        let slideInterval;

        // Criar pontos de navegação
        slides.forEach((_, i) => {
            const dot = document.createElement('button');
            dot.classList.add('dot');
            if (i === 0) dot.classList.add('active');
            dot.addEventListener('click', () => {
                goToSlide(i);
                resetInterval();
            });
            dotsContainer.appendChild(dot);
        });
        const dots = document.querySelectorAll('.dot');

        function updateDots(index) {
            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === index);
            });
        }
        
        function goToSlide(index) {
            if (index < 0) {
                index = slides.length - 1;
            } else if (index >= slides.length) {
                index = 0;
            }
            carouselWrapper.style.transform = `translateX(-${index * 100}%)`;
            currentIndex = index;
            updateDots(currentIndex);
        }

        prevBtn.addEventListener('click', () => {
            goToSlide(currentIndex - 1);
            resetInterval();
        });

        nextBtn.addEventListener('click', () => {
            goToSlide(currentIndex + 1);
            resetInterval();
        });

        function startInterval() {
           slideInterval = setInterval(() => {
                goToSlide(currentIndex + 1);
            }, 5000); // Mudar slide a cada 5 segundos
        }
        
        function resetInterval() {
            clearInterval(slideInterval);
            startInterval();
        }

        startInterval();
    }
});