function sendRecoveryEmail() {
    const email = document.getElementById('email').value;
    // Simula validação do email (substitua por sua lógica real)
    if (email && email.includes('@')) {
        // Abre o Outlook Web com nova mensagem para o email informado
        window.open(`https://outlook.live.com/mail/0/?compose=1&to=${encodeURIComponent(email)}&subject=Recuperação de Senha&body=Clique no link para recuperar sua senha: [INSIRA O LINK AQUI]`, '_blank');
        document.getElementById('message').textContent = "Uma nova janela do Outlook foi aberta para continuar a recuperação.";
        return true; // Permite o envio do formulário se necessário
    } else {
        alert("E-mail inválido.");
        document.getElementById('message').textContent = "Por favor, insira um e-mail válido.";
    }
    return false; // Impede o envio do formulário
}