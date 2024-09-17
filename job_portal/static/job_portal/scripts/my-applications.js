document.addEventListener("DOMContentLoaded", function () {
    const mainContainer = document.getElementById("main-container");
    const toggleButton = document.getElementById("toggle-button");
    const extraInfo = document.getElementById("extra-info");

    toggleButton.addEventListener("click", function () {
        mainContainer.classList.toggle('visible');

        if (extraInfo.classList.contains("visible")) {
            extraInfo.classList.remove("visible");
            toggleButton.textContent = "Show More";
        } else {
            extraInfo.classList.add("visible");
            toggleButton.textContent = "Show Less";
        }
    });
});