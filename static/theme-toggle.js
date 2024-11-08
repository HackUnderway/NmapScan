// theme-toggle.js

document.addEventListener("DOMContentLoaded", function () {
    const toggleSwitch = document.getElementById("theme-toggle");
    const themeLabel = document.getElementById("theme-label");

    // Load the user's theme preference from localStorage
    const currentTheme = localStorage.getItem("theme") || "dark";
    if (currentTheme === "light") {
        document.body.classList.add("light-theme");
        toggleSwitch.checked = true;
        themeLabel.textContent = "Light Mode";
    } else {
        themeLabel.textContent = "Dark Mode";
    }

    // Toggle the theme and save the preference
    toggleSwitch.addEventListener("change", function () {
        document.body.classList.toggle("light-theme");
        const theme = document.body.classList.contains("light-theme") ? "light" : "dark";
        localStorage.setItem("theme", theme);
        themeLabel.textContent = theme === "light" ? "Light Mode" : "Dark Mode";
    });
});
