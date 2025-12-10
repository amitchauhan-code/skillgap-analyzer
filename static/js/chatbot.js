document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("chatbot-toggle");
  const popup = document.getElementById("chatbot-popup");
  const close = document.getElementById("chatbot-close");

  toggle.addEventListener("click", () => {
    popup.classList.toggle("active");
  });

  close.addEventListener("click", () => {
    popup.classList.remove("active");
  });
});