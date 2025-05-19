// ************ Funções para filtrar os livros *********************
function filtrarLivros() {
    const generosSelecionados = Array.from(
        document.querySelectorAll('input[name="genero"]:checked')
    ).map(cb => cb.value.toLowerCase());

    const termoBusca = document.getElementById('termo-busca').value.toLowerCase();

    document.querySelectorAll('.livro').forEach(livro => {
        const generoLivro = livro.getAttribute('data-genero').toLowerCase();
        const nomeLivroTexto = livro.getAttribute('data-nome').toLowerCase();
        const autorLivroTexto = livro.getAttribute('data-autor').toLowerCase();

        const correspondeGeneroSelecionado = generosSelecionados.length === 0 || 
                                             generosSelecionados.includes(generoLivro);

        const generoLivroNome = livro.getAttribute('data-genero-nome');

        const correspondeBusca =
            nomeLivroTexto.includes(termoBusca) ||
            autorLivroTexto.includes(termoBusca) ||
            generoLivroNome.includes(termoBusca);


        livro.style.display = (correspondeGeneroSelecionado && correspondeBusca)
                           ? ''
                           : 'none';
    });
}


// ********* Submenu ao passar o mouse (integrado com Django) ***********
function configurarSubmenu() {
    const perfilBtn = document.querySelector('.perfil-btn');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    // Função para pegar cookie (necessária para o CSRF token)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Função para atualizar o submenu
    function atualizarSubmenu() {
        if (!dropdownMenu) return;

        dropdownMenu.innerHTML = window.djangoAuth.isAuthenticated
            ? `
                <li><a href="${window.djangoAuth.minhaContaUrl}">Minha Conta</a></li>
                <li><a href="#" id="sair">Sair</a></li>
              `
            : `
                <li><a href="${window.djangoAuth.loginUrl}">Fazer Login</a></li>
                <li><a href="${window.djangoAuth.signupUrl}">Criar Conta</a></li>
              `;

        // Adiciona evento de logout
        const sairBtn = document.getElementById('sair');
        if (sairBtn) {
            sairBtn.addEventListener('click', (e) => {
                e.preventDefault();
                // Cria um formulário de logout dinâmico
                const form = document.createElement('form');
                form.method = 'POST';
                form.action = window.djangoAuth.logoutUrl;
                
                // Adiciona o CSRF token
                const csrfInput = document.createElement('input');
                csrfInput.type = 'hidden'; 
                csrfInput.name = 'csrfmiddlewaretoken';
                csrfInput.value = getCookie('csrftoken');
                form.appendChild(csrfInput);
                
                document.body.appendChild(form);
                form.submit();
            });
        }
    }

    // Eventos de hover
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

    // Inicializa o submenu
    if (dropdownMenu) {
        dropdownMenu.style.display = 'none';
        atualizarSubmenu();
    }
}

// ****************** Modo Claro/Escuro ******************
function configurarTema() {
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

// ************** Inicialização quando o DOM carrega **************
document.addEventListener('DOMContentLoaded', function() {
    // Filtro por input e botão de busca
    const campoBusca = document.getElementById('termo-busca');
    const botaoBuscar = document.getElementById('buscar');

    if (campoBusca) campoBusca.addEventListener('input', filtrarLivros);
    if (botaoBuscar) botaoBuscar.addEventListener('click', filtrarLivros);

    // Configura o submenu
    configurarSubmenu();

    // Configura o tema
    configurarTema();
});

// ************** Validação do formulário de login **************
if (document.getElementById('login-form')) {
    document.getElementById('login-form').addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('email')?.value;
        const senha = document.getElementById('senha')?.value;

        if (!email || !senha) {
            alert('Preencha todos os campos!');
            return;
        }

        // Validação básica de e-mail
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            alert('Por favor, insira um e-mail válido.');
            return;
        }

        // Se passou na validação, envia o formulário
        this.submit();
    });
}
