// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    
    // ... (código existente de outras páginas) ...

    // --- LÓGICA DA FRENTE DE CAIXA ---
    /**
     * Seleciona o elemento HTML que representa o container principal da página de caixa.
     * @type {Element|null}
     * Retorna o elemento com a classe 'caixa-page-container', ou null se não existir.
     * Este elemento é utilizado para manipular ou acessar funcionalidades específicas da página de caixa.
     */
    const caixaPage = document.querySelector('.caixa-page-container');
    if (caixaPage) {
        // Simulação de dados do backend
        const openOrders = [
            { id: 1, name: 'Mesa 02', total: 110.00, items: [{qty: 2, name: 'Pizza Média', price: 45.00}, {qty: 1, name: 'Refrigerante 2L', price: 20.00}] },
            { id: 2, name: 'Mesa 06', total: 215.50, items: [{qty: 1, name: 'Picanha na Chapa', price: 150.00}, {qty: 2, name: 'Cerveja Artesanal', price: 25.00}, {qty: 1, name: 'Sobremesa', price: 15.50}] },
            { id: 3, name: 'Comanda #34', total: 45.00, items: [{qty: 1, name: 'Hambúrguer Gourmet', price: 35.00}, {qty: 1, name: 'Suco Natural', price: 10.00}] },
        ];

        const comandasList = document.querySelector('.comandas-list');
        const detalhesContent = document.getElementById('detalhes-content');
        const pagamentoPanel = document.getElementById('panel-pagamento');
        const pagamentoTotal = document.getElementById('pagamento-total');
        const btnFinalizar = document.getElementById('btn-finalizar');

        function renderOrderList() {
            comandasList.innerHTML = '';
            openOrders.forEach(order => {
                const li = document.createElement('li');
                li.className = 'comanda-item';
                li.dataset.id = order.id;
                li.innerHTML = `
                    <span class="comanda-id">${order.name}</span>
                    <span class="comanda-total">R$ ${order.total.toFixed(2)}</span>
                `;
                li.addEventListener('click', () => selectOrder(order.id));
                comandasList.appendChild(li);
            });
        }

        function selectOrder(orderId) {
            // Remove 'active' de todos os itens
            document.querySelectorAll('.comanda-item').forEach(item => item.classList.remove('active'));
            // Adiciona 'active' no item clicado
            document.querySelector(`.comanda-item[data-id='${orderId}']`).classList.add('active');

            const order = openOrders.find(o => o.id === orderId);
            renderOrderDetails(order);
            activatePaymentPanel(order);
        }
        
        function renderOrderDetails(order) {
            let itemsHtml = `
                <table class="item-table">
                    <thead><tr><th>Qtd</th><th>Item</th><th class="price">Preço</th></tr></thead>
                    <tbody>`;
            order.items.forEach(item => {
                itemsHtml += `
                    <tr>
                        <td class="qty">${item.qty}x</td>
                        <td>${item.name}</td>
                        <td class="price">R$ ${(item.qty * item.price).toFixed(2)}</td>
                    </tr>
                `;
            });
            itemsHtml += `
                    </tbody>
                </table>
                <div class="bill-summary">
                    <p>Subtotal: R$ ${order.total.toFixed(2)}</p>
                    <p>Serviço (10%): R$ ${(order.total * 0.1).toFixed(2)}</p>
                    <h3>Total: R$ ${(order.total * 1.1).toFixed(2)}</h3>
                </div>
            `;
            detalhesContent.innerHTML = itemsHtml;
        }

        function activatePaymentPanel(order) {
            const finalTotal = order.total * 1.1;
            pagamentoPanel.classList.remove('disabled-panel');
            pagamentoTotal.textContent = `R$ ${finalTotal.toFixed(2)}`;
            btnFinalizar.disabled = false;
        }

        btnFinalizar.addEventListener('click', () => {
            alert('Pagamento finalizado com sucesso!');
            // Aqui iria a lógica para remover a ordem da lista, limpar os painéis, etc.
            location.reload(); // Simplesmente recarrega a página para simular a atualização
        });

        renderOrderList();
    }
});