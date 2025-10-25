document.addEventListener('DOMContentLoaded', function() {
    // Validação do formulário
    const form = document.getElementById('cityForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            const nome = document.getElementById('nome').value.trim();
            const uf = document.getElementById('uf').value.trim();

            if (!nome || !uf) {
                e.preventDefault();
                showAlert('Por favor, preencha todos os campos', 'error');
                return;
            }

            if (uf.length !== 2) {
                e.preventDefault();
                showAlert('UF deve ter exatamente 2 letras', 'error');
                return;
            }
        });
    }

    // Função para mostrar alertas
    window.showAlert = function(message, type) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} fade-in`;
        alertDiv.textContent = message;

        const container = document.querySelector('.container');
        container.insertBefore(alertDiv, container.firstChild);

        setTimeout(() => {
            alertDiv.style.opacity = '0';
            setTimeout(() => alertDiv.remove(), 300);
        }, 3000);
    }

    // Filtro de pesquisa na tabela
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            const rows = document.querySelectorAll('table tbody tr');

            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(searchTerm) ? '' : 'none';
            });
        });
    }

    // Formatação automática de UF para maiúsculas
    const ufInput = document.getElementById('uf');
    if (ufInput) {
        ufInput.addEventListener('input', function() {
            this.value = this.value.toUpperCase();
        });
    }

    // Confirmação de exclusão
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Tem certeza que deseja excluir esta cidade?')) {
                e.preventDefault();
            }
        });
    });
});