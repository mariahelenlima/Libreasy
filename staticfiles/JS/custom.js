document.addEventListener("DOMContentLoaded", function () {
    let passwordFields = document.querySelectorAll("input[type='password']");

    passwordFields.forEach((field) => {
        let wrapper = document.createElement("div");
        wrapper.style.position = "relative";
        wrapper.style.display = "flex";
        wrapper.style.alignItems = "center";

        let eyeIcon = document.createElement("span");
        eyeIcon.innerHTML = "&#128065;"; // Ícone de olho
        eyeIcon.style.position = "absolute";
        eyeIcon.style.right = "10px";
        eyeIcon.style.cursor = "pointer";
        eyeIcon.style.fontSize = "18px";

        eyeIcon.addEventListener("click", function () {
            field.type = field.type === "password" ? "text" : "password";
        });

        field.parentNode.insertBefore(wrapper, field);
        wrapper.appendChild(field);
        wrapper.appendChild(eyeIcon);
    });
});
