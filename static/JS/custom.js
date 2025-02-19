document.addEventListener("DOMContentLoaded", function () {
    let passwordFields = document.querySelectorAll("input[type='password']");

    passwordFields.forEach((field) => {
        let eyeIcon = document.createElement("span");
        eyeIcon.innerHTML = "&#128065;"; // Ícone de olho
        eyeIcon.style.position = "absolute";
        eyeIcon.style.right = "41px";
        eyeIcon.style.cursor = "pointer";
        eyeIcon.style.fontSize = "18px";
        eyeIcon.style.transform = "translateY(-50%)";
        eyeIcon.style.top = "50%";

        eyeIcon.addEventListener("click", function () {
            field.type = field.type === "password" ? "text" : "password";
        });

        field.style.paddingRight = "35px"; // Ajusta o espaço para o ícone
        field.parentNode.style.position = "relative"; // Garante que o pai do input seja relativo
        field.parentNode.appendChild(eyeIcon); // Adiciona o ícone dentro do container do input
    });
});
