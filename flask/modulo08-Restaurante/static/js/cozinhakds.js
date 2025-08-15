// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    
    // ... (código existente de outras páginas) ...

    // --- LÓGICA DO PAINEL DA COZINHA (KDS) ---
    const kdsPage = document.querySelector('.kds-page-container');
    if (kdsPage) {
        const colTodo = document.getElementById('col-todo');
        const colInProgress = document.getElementById('col-in-progress');
        const colReady = document.getElementById('col-ready');
        const cardTemplate = document.getElementById('kds-card-template');
        const notificationSound = document.getElementById('notification-sound');
        const soundEnabled = document.getElementById('sound-check');
        const clockEl = document.getElementById('kds-clock');
        
        // Simulação de Pedidos
        const sampleOrders = [
            { table: 'Mesa 05', items: ['2x Hambúrguer da Casa<small>- Sem picles</small>', '1x Porção de Fritas'] },
            { table: 'Mesa 12', items: ['1x Filé à Parmegiana', '1x Suco de Laranja'] },
            { table: 'Delivery #102', items: ['1x Pizza Calabresa<small>- Borda recheada</small>', '1x Coca-Cola 2L'] },
        ];
        let orderCounter = 0;

        function addOrder() {
            if(sampleOrders.length === 0) return;
            const orderData = sampleOrders.shift(); // Pega o primeiro e remove da lista

            const card = cardTemplate.content.cloneNode(true).firstElementChild;
            card.dataset.startTime = new Date().getTime();
            card.querySelector('.card-table').textContent = orderData.table;
            
            const itemsList = card.querySelector('.card-items');
            orderData.items.forEach(itemText => {
                const li = document.createElement('li');
                li.innerHTML = itemText;
                itemsList.appendChild(li);
            });

            colTodo.appendChild(card);
            
            if (soundEnabled.checked) {
                notificationSound.currentTime = 0;
                notificationSound.play();
            }
        }

        // Simula a chegada de um novo pedido a cada 15 segundos
        setInterval(addOrder, 15000);

        // Atualizador de Timers e Relógio
        setInterval(() => {
            // Atualiza o relógio principal
            clockEl.textContent = new Date().toLocaleTimeString('pt-BR');

            // Atualiza os timers de cada card
            document.querySelectorAll('.kds-card').forEach(card => {
                const startTime = parseInt(card.dataset.startTime, 10);
                const elapsedSeconds = Math.floor((new Date().getTime() - startTime) / 1000);
                
                const minutes = Math.floor(elapsedSeconds / 60).toString().padStart(2, '0');
                const seconds = (elapsedSeconds % 60).toString().padStart(2, '0');
                
                const timerEl = card.querySelector('.card-timer');
                timerEl.textContent = `${minutes}:${seconds}`;

                // Alerta de cor
                timerEl.classList.remove('warning', 'late');
                if (elapsedSeconds > 600) { // 10 minutos
                    timerEl.classList.add('late');
                } else if (elapsedSeconds > 300) { // 5 minutos
                    timerEl.classList.add('warning');
                }
            });

        }, 1000);

        // Mover cards entre colunas (usando delegação de eventos)
        kdsPage.addEventListener('click', function(e) {
            if (e.target.classList.contains('btn-card-action')) {
                const card = e.target.closest('.kds-card');// 
                const currentColumn = card.parentElement;
                
                if (currentColumn.id === 'col-todo') {
                    e.target.textContent = 'Finalizar Pedido';
                    colInProgress.appendChild(card);
                } else if (currentColumn.id === 'col-in-progress') {
                    e.target.textContent = 'Retirado pelo Garçom';
                    colReady.appendChild(card);
                } else if (currentColumn.id === 'col-ready') {
                    card.classList.add('done');
                    // Remove o card do DOM após a animação de fade-out
                    card.addEventListener('animationend', () => card.remove());
                }
            }
        });
        
        // Adiciona um pedido inicial para demonstração
        addOrder();
    }
});