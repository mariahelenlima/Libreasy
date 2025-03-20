// Estado de login (simulação)
let usuarioLogado = false; // Altere para true para simular usuário logado

// Função para atualizar o submenu de "Minha Conta"
function atualizarSubmenu() {
    const dropdownMenu = document.querySelector(".dropdown-menu");
    dropdownMenu.innerHTML = ""; // Limpa o submenu

    if (usuarioLogado) {
        // Opções para usuário logado
        dropdownMenu.innerHTML = `
            <li><a href="emprestimos.html">Meus Empréstimos</a></li>
            <li><a href="meus-dados.html">Meus Dados</a></li>
            <li><a href="#" id="sair">Sair</a></li>
        `;
        document.getElementById("sair").addEventListener("click", () => {
            fetch("/logout/", { method: "POST" })  // Faz logout no backend
                .then(() => {
                    usuarioLogado = false;
                    atualizarSubmenu();
                });
        });
    } else {
        // Opções para usuário não logado
        dropdownMenu.innerHTML = `
            <li><a href="#" id="fazer-login">Fazer Login</a></li>
            <li><a href="criar-conta/">Criar Conta</a></li>
        `;
        document
            .getElementById("fazer-login")
            .addEventListener("click", (e) => {
                e.preventDefault();
                document.getElementById("login-popup").style.display = "flex";
            });
    }
}

// Pop-up de Login
const loginPopup = document.getElementById("login-popup");
const closePopup = document.querySelector(".close-popup");
const loginForm = document.getElementById("login-form");

closePopup.addEventListener("click", () => {
    loginPopup.style.display = "none";
});

loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const usuario = document.getElementById("usuario").value;
    const senha = document.getElementById("senha").value;

    // Envia os dados de login para o backend
    fetch("/login/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value, // Adiciona o token CSRF
        },
        body: JSON.stringify({ username: usuario, password: senha }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                usuarioLogado = true;
                atualizarSubmenu();
                loginPopup.style.display = "none";
            } else {
                alert(data.error || "Usuário ou senha inválidos.");
            }
        })
        .catch((error) => {
            console.error("Erro ao fazer login:", error);
        });
});

// Fechar pop-up ao clicar fora
window.addEventListener("click", (e) => {
    if (e.target === loginPopup) {
        loginPopup.style.display = "none";
    }
});

// Submenu ao passar o mouse
const minhaContaBtn = document.querySelector(".minha-conta-btn");
const dropdownMenu = document.querySelector(".dropdown-menu");

minhaContaBtn.addEventListener("mouseenter", () => {
    dropdownMenu.style.display = "block";
});

minhaContaBtn.addEventListener("mouseleave", () => {
    dropdownMenu.style.display = "none";
});

dropdownMenu.addEventListener("mouseenter", () => {
    dropdownMenu.style.display = "block";
});

dropdownMenu.addEventListener("mouseleave", () => {
    dropdownMenu.style.display = "none";
});

// Inicializa o submenu
atualizarSubmenu();