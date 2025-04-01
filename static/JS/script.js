// ************ Funções para filtrar os livros *********************
function filtrarLivros() {
    const generosSelecionados = Array.from(
        document.querySelectorAll('input[name="genero"]:checked')
    ).map(cb => cb.value);

    const termoBusca = document.getElementById('termo-busca').value.toLowerCase();

    document.querySelectorAll('.livro').forEach(livro => {
        const generoLivro = livro.getAttribute('data-genero');
        const nomeLivroTexto = livro.getAttribute('data-nome').toLowerCase();
        const autorLivroTexto = livro.getAttribute('data-autor').toLowerCase();

        const correspondeGenero = generosSelecionados.length === 0 || 
                                  generosSelecionados.includes(generoLivro);
        const correspondeBusca = nomeLivroTexto.includes(termoBusca) || autorLivroTexto.includes(termoBusca);

        livro.style.display = (correspondeGenero && correspondeBusca) 
                           ? 'block' 
                           : 'none';
    });
}

//Event Listener
document.addEventListener('DOMContentLoaded', function() {
    // Filtro por input e botão de busca
    const campoBusca = document.getElementById('termo-busca');
    const botaoBuscar = document.getElementById('buscar');

    campoBusca.addEventListener('input', filtrarLivros);
    botaoBuscar.addEventListener('click', filtrarLivros);
});

// ********* Submenu ao passar o mouse ***********
const minhaContaBtn = document.querySelector('.minha-conta-btn');
const dropdownMenu = document.querySelector('.dropdown-menu');

if (minhaContaBtn && dropdownMenu) {
    minhaContaBtn.addEventListener('mouseenter', () => {
        dropdownMenu.style.display = 'block';
    });

    minhaContaBtn.addEventListener('mouseleave', () => {
        dropdownMenu.style.display = 'none';
    });

    dropdownMenu.addEventListener('mouseenter', () => {
        dropdownMenu.style.display = 'block';
    });

    dropdownMenu.addEventListener('mouseleave', () => {
        dropdownMenu.style.display = 'none';
    });
}

// Modo Claro/Escuro
window.onload = function () {
    const themeToggle = document.getElementById('theme-toggle');

    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        if (currentTheme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'light');
            themeToggle.textContent = '🌙';
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeToggle.textContent = '☀️';
            localStorage.setItem('theme', 'dark');
        }
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeToggle.textContent = '☀️';
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            themeToggle.textContent = '🌙';
        }
    }
}

// ************ Pop-up de Login ********************
// (Mantém código relacionado ao pop-up inalterado)

// ************ Pop-up de Login ********************
const loginPopup = document.getElementById('login-popup');
const closePopup = document.querySelector('.close-popup');
const loginForm = document.getElementById('login-form');
const loginButtons = document.querySelectorAll('#fazer-login'); // Seleciona todos os botões de login

// Abrir pop-up ao clicar em qualquer botão "Fazer Login"
if (loginButtons) {
    loginButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            loginPopup.style.display = 'flex';
        });
    });
}

// Fechar pop-up ao clicar no botão de fechar
if (closePopup) {
    closePopup.addEventListener('click', () => {
        loginPopup.style.display = 'none';
        loginForm.reset(); // Reseta o formulário
    });
}

// Fechar pop-up ao clicar fora dele
window.addEventListener('click', (e) => {
    if (e.target === loginPopup) {
        loginPopup.style.display = 'none';
        loginForm.reset(); // Reseta o formulário
    }
});

// Fechar pop-up ao pressionar a tecla "Esc"
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && loginPopup.style.display === 'flex') {
        loginPopup.style.display = 'none';
        loginForm.reset(); // Reseta o formulário
    }
});

// Validação do formulário de login
if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('email')?.value;
        const senha = document.getElementById('senha')?.value;

        if (!email || !senha) {
            alert('Preencha todos os campos!');
            return;
        }

        // Validação básica de e-mail
        if (!validateEmail(email)) {
            alert('Por favor, insira um e-mail válido.');
            return;
        }

        // Simulação de login bem-sucedido
        alert('Login realizado com sucesso!');
        loginPopup.style.display = 'none';
        loginForm.reset(); // Reseta o formulário
    });
}

// Função para validar e-mail
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}
