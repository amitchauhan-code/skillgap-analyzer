document.addEventListener("DOMContentLoaded", () => {
  // ScrollReveal
  ScrollReveal().reveal('.reveal', {
    delay: 200,
    distance: '50px',
    origin: 'bottom',
    interval: 200,
    easing: 'cubic-bezier(0.175, 0.885, 0.32, 1.275)'
  });

  // 3D Tilt
  VanillaTilt.init(document.querySelectorAll("[data-tilt]"), {
    max: 15,
    speed: 400,
    glare: true,
    "max-glare": 0.5,
  });
});