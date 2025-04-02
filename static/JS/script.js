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

// Estado de login (simulação - real = logado / false = deslogado)
let usuarioLogado = true;

// Elementos do DOM
const perfilBtn = document.querySelector('.perfil-btn');
const dropdownMenu = document.querySelector('.dropdown-menu');
const loginUrl = dropdownMenu.getAttribute('data-url-login');
const criarContaUrl = dropdownMenu.getAttribute('data-url-criar-conta');
const minhaContaUrl = dropdownMenu.getAttribute('data-url-minha-conta');


// Função para atualizar o submenu
function atualizarSubmenu() {
    if (!dropdownMenu) return;

    dropdownMenu.innerHTML = usuarioLogado
        ? `
            <li><a href="${minhaContaUrl}">Minha Conta</a></li>
            <li><a href="#" id="sair">Sair</a></li>
          `
        : `
            <li><a href="${loginUrl}">Fazer Login</a></li>
            <li><a href="${criarContaUrl}">Criar Conta</a></li>
          `;

    // Adiciona evento de logout se existir
    const sairBtn = document.getElementById('sair');
    if (sairBtn) {
        sairBtn.addEventListener('click', (e) => {
            e.preventDefault();
            usuarioLogado = false;
            atualizarSubmenu();
        });
    }
}

// Eventos de hover (se os elementos existirem)
if (perfilBtn && dropdownMenu) {
    perfilBtn.addEventListener('mouseenter', () => {
        dropdownMenu.style.display = 'block';
    });

    perfilBtn.addEventListener('mouseleave', () => {
        dropdownMenu.style.display = 'none';
    });

    dropdownMenu.addEventListener('mouseenter', () => {
        dropdownMenu.style.display = 'block';
    });

    dropdownMenu.addEventListener('mouseleave', () => {
        dropdownMenu.style.display = 'none';
    });
}

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    dropdownMenu.style.display = 'none'; // Garante que inicia fechado
    atualizarSubmenu();
});


// ****************** Modo Claro/Escuro ******************
window.onload = function () {
    const themeToggle = document.getElementById('theme-toggle');

    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        if (currentTheme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'light');
            themeToggle.textContent = '☀️';
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeToggle.textContent = '🌙';
            localStorage.setItem('theme', 'dark');
        }
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeToggle.textContent = '🌙';
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
            themeToggle.textContent = '☀️';
        }
    }
}


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
