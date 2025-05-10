document.addEventListener("DOMContentLoaded", function () {
    let passwordFields = document.querySelectorAll("input[type='password']");

    passwordFields.forEach((field) => {
        // Cria container para o ícone (melhor prática)
        let iconContainer = document.createElement("div");
        iconContainer.style.position = "relative";
        //iconContainer.style.display = "inline-block"; // Mantém o comportamento do input
        
        iconContainer.style.display = "block";
        iconContainer.style.width = "85%";


        // Envolve o input no container
        field.parentNode.insertBefore(iconContainer, field);
        iconContainer.appendChild(field);

        // Cria o ícone do olho
        let eyeIcon = document.createElement("span");
        eyeIcon.innerHTML = "👁"; // Ou &#128065;
        eyeIcon.style.position = "absolute";
        eyeIcon.style.right = "20px"; // Ajuste este valor conforme necessário
        eyeIcon.style.top = "50%";
        eyeIcon.style.transform = "translateY(-50%)";
        eyeIcon.style.cursor = "pointer";
        eyeIcon.style.fontSize = "18px";
        eyeIcon.style.color = "#666"; // Cor mais discreta
        eyeIcon.style.userSelect = "none"; // Evita seleção acidental
        
        // Ajusta o input
        field.style.paddingRight = "50px"; // Espaço para o ícone
        field.style.boxSizing = "border-box"; // Garante que o padding não aumente o tamanho total
        field.style.width = "100%";

        // Adiciona o ícone
        iconContainer.appendChild(eyeIcon);

        // Funcionalidade de mostrar/ocultar
        eyeIcon.addEventListener("click", function () {
            field.type = field.type === "password" ? "text" : "password";
            // Opcional: mudar o ícone quando a senha estiver visível
            eyeIcon.innerHTML = field.type === "password" ? "👁" : "👀";
        });
    });
});