// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {

    // --- LÓGICA DA TELA DE PEDIDOS ---
    const categoryPanel = document.getElementById('category-panel');
    const productPanel = document.getElementById('product-panel');
    const comandaItemsEl = document.getElementById('comanda-items');
    const comandaTotalEl = document.getElementById('comanda-total');

    if (categoryPanel) {
        // Dados de exemplo (simulando um banco de dados)
        const menu = {
            "Entradas": [
                { nome: "Coxinha (un)", preco: 8.00 },
                { nome: "Batata Frita", preco: 25.00 },
            ],
            "Pratos Principais": [
                { nome: "Filé à Parmegiana", preco: 62.00 },
                { nome: "Lasanha Bolonhesa", preco: 55.00 },
            ],
            "Bebidas": [
                { nome: "Coca-Cola Zero", preco: 7.00 },
                { nome: "Suco de Laranja", preco: 9.50 },
            ]
        };

        const comanda = [];

        function updateTotal() {
            const total = comanda.reduce((sum, item) => sum + item.preco, 0);
            comandaTotalEl.textContent = `Total: R$ ${total.toFixed(2)}`;
        }

        function renderComanda() {
            comandaItemsEl.innerHTML = '';
            comanda.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `${item.nome} - R$ ${item.preco.toFixed(2)}`;
                comandaItemsEl.appendChild(li);
            });
            updateTotal();
        }

        function renderProducts(category) {
            const productList = productPanel.querySelector('.product-list');
            productList.innerHTML = '';
            menu[category].forEach(product => {
                const li = document.createElement('li');
                li.textContent = `${product.nome} - R$ ${product.preco.toFixed(2)}`;
                li.addEventListener('click', () => {
                    comanda.push(product);
                    renderComanda();
                });
                productList.appendChild(li);
            });
        }

        const categoryList = categoryPanel.querySelector('.category-list');
        Object.keys(menu).forEach(category => {
            const li = document.createElement('li');
            li.textContent = category;
            li.addEventListener('click', () => {
                // Remove a classe 'active' de todos
                categoryList.querySelectorAll('li').forEach(item => item.classList.remove('active'));
                // Adiciona no item clicado
                li.classList.add('active');
                renderProducts(category);
            });
            categoryList.appendChild(li);
        });

        // Inicia com a primeira categoria selecionada
        categoryList.querySelector('li').click();
    }

    // --- LÓGICA DOS RELATÓRIOS ---
    const chartCanvas = document.getElementById('topSellersChart');
    if (chartCanvas) {
        const ctx = chartCanvas.getContext('2d');
        const topSellersChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Filé à Parmegiana', 'Hambúrguer da Casa', 'Coca-Cola Zero', 'Batata Frita'],
                datasets: [{
                    label: '# de Vendas',
                    data: [120, 95, 70, 65],
                    backgroundColor: [
                        'rgba(211, 47, 47, 0.7)',
                        'rgba(56, 142, 60, 0.7)',
                        'rgba(25, 118, 210, 0.7)',
                        'rgba(251, 192, 45, 0.7)',
                    ],
                    borderColor: [
                        'rgba(211, 47, 47, 1)',
                        'rgba(56, 142, 60, 1)',
                        'rgba(25, 118, 210, 1)',
                        'rgba(251, 192, 45, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                indexAxis: 'y', // Para criar um gráfico de barras horizontais
            }
        });
    }

});
function validarLogin() {
    const usuario = document.getElementById('username').value.trim();
    const senha = document.getElementById('password').value.trim();
    if (usuario === "" || senha === "") {
        alert("Por favor, preencha usuário e senha.");
        return false;
    }
    else if (senha.length < 4) {
        alert("A senha deve ter pelo menos 4 caracteres.");
        return false;
    }
    else {
        // Adicione aqui validações adicionais se necessário
        if (usuario !== "admin" || senha !== "admin123") {
            alert("Usuário ou senha incorretos.");
            return false;
        }
        alert("Login realizado com sucesso!");
        return true;
    }
}