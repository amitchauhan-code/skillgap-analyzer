// FINAL THEME.JS - Safe & Beautiful
document.addEventListener("DOMContentLoaded", () => {
    const html = document.documentElement;
    const toggle = document.getElementById("theme-toggle");

    // Default light mode
    let theme = localStorage.getItem("theme") || "light";
    html.setAttribute("data-theme", theme);

    // Icon set karo
    toggle.innerHTML = theme === "dark" 
        ? '<i class="fas fa-sun"></i>' 
        : '<i class="fas fa-moon"></i>';

    toggle.addEventListener("click", () => {
        theme = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
        html.setAttribute("data-theme", theme);
        localStorage.setItem("theme", theme);
        toggle.innerHTML = theme === "dark" 
            ? '<i class="fas fa-sun"></i>' 
            : '<i class="fas fa-moon"></i>';
    });
});