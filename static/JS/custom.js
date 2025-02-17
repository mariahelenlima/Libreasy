document.addEventListener("DOMContentLoaded", function () {
    let passwordFields = document.querySelectorAll("input[type='password']");

    passwordFields.forEach((field) => {
        let wrapper = document.createElement("div");
        wrapper.style.position = "relative";
        wrapper.style.display = "inline-block"; // Mantém o tamanho do input
        wrapper.style.width = field.offsetWidth + "px"; // Mantém a largura do input

        let eyeIcon = document.createElement("span");
        eyeIcon.innerHTML = "&#128064;"; // Ícone de olho
        eyeIcon.style.position = "absolute";
        eyeIcon.style.right = "10px";
        eyeIcon.style.cursor = "pointer";
        eyeIcon.style.top = "50%";
        eyeIcon.style.transform = "translateY(-50%)";
        eyeIcon.style.fontSize = "18px";

        eyeIcon.addEventListener("click", function () {
            field.type = field.type === "password" ? "text" : "password";
        });

        field.parentNode.insertBefore(wrapper, field);
        wrapper.appendChild(field);
        wrapper.appendChild(eyeIcon);
    });
});
