document.addEventListener('DOMContentLoaded', function() {
    // Validação de formulário
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const amountInput = form.querySelector('input[name="amount"]');
            if (amountInput) {
                const amount = parseFloat(amountInput.value);
                if (isNaN(amount) || amount <= 0) {
                    e.preventDefault();
                    showAlert('Por favor, insira um valor positivo válido', 'error');
                }
            }
        });
    });

    // Manipulação de mensagens flash
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});

function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    setTimeout(() => {
        alertDiv.style.opacity = '0';
        setTimeout(() => alertDiv.remove(), 300);
    }, 5000);
}

// Formatar moeda
function formatCurrency(amount) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(amount);
}

// Atualizar saldo em tempo real após transações
function updateBalance(newBalance) {
    const balanceElement = document.querySelector('.balance-amount');
    if (balanceElement) {
        balanceElement.textContent = formatCurrency(newBalance);
    }
}