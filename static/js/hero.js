document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".hero-slider .slide");
  const dotsContainer = document.querySelector(".slider-dots");
  let current = 0;

  if (!slides.length) return;

  // Create dots
  slides.forEach((_, i) => {
    const dot = document.createElement("div");
    dot.classList.add("dot");
    if (i === 0) dot.classList.add("active");
    dot.addEventListener("click", () => goToSlide(i));
    dotsContainer.appendChild(dot);
  });

  const dots = document.querySelectorAll(".dot");

  function goToSlide(n) {
    slides[current].classList.remove("active");
    dots[current].classList.remove("active");
    current = n;
    slides[current].classList.add("active");
    dots[current].classList.add("active");
  }

  setInterval(() => {
    let next = (current + 1) % slides.length;
    goToSlide(next);
  }, 5000);
});