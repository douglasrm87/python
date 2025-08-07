// Sistema de Autenticação
class AuthSystem {
    constructor() {
        this.currentUser = null;
        this.users = this.loadUsers();
        this.init();
    }

    init() {
        // Verificar se há usuário logado
        const savedUser = localStorage.getItem('currentUser');
        if (savedUser) {
            this.currentUser = JSON.parse(savedUser);
        }
    }

    loadUsers() {
        // Carregar usuários do localStorage ou criar dados padrão
        const savedUsers = localStorage.getItem('users');
        if (savedUsers) {
            return JSON.parse(savedUsers);
        }

        // Dados padrão para demonstração
        const defaultUsers = [
            {
                id: 1,
                email: 'morador@smartcondo.com',
                cpf: '123.456.789-00',
                password: '123456',
                name: 'João Silva',
                role: 'morador',
                apartment: '101',
                block: 'A',
                phone: '(11) 99999-9999',
                avatar: null,
                active: true,
                createdAt: new Date().toISOString()
            },
            {
                id: 2,
                email: 'sindico@smartcondo.com',
                cpf: '987.654.321-00',
                password: '123456',
                name: 'Maria Santos',
                role: 'sindico',
                apartment: '205',
                block: 'B',
                phone: '(11) 88888-8888',
                avatar: null,
                active: true,
                createdAt: new Date().toISOString()
            },
            {
                id: 3,
                email: 'admin@smartcondo.com',
                cpf: '111.222.333-44',
                password: '123456',
                name: 'Carlos Administrador',
                role: 'admin',
                apartment: null,
                block: null,
                phone: '(11) 77777-7777',
                avatar: null,
                active: true,
                createdAt: new Date().toISOString()
            },
            {
                id: 4,
                email: 'porteiro@smartcondo.com',
                cpf: '555.666.777-88',
                password: '123456',
                name: 'Pedro Porteiro',
                role: 'porteiro',
                apartment: null,
                block: null,
                phone: '(11) 66666-6666',
                avatar: null,
                active: true,
                createdAt: new Date().toISOString()
            }
        ];

        this.saveUsers(defaultUsers);
        return defaultUsers;
    }

    saveUsers(users) {
        localStorage.setItem('users', JSON.stringify(users));
    }

    login(emailOrCpf, password) {
        const user = this.users.find(u => 
            (u.email === emailOrCpf || u.cpf === emailOrCpf) && 
            u.password === password && 
            u.active
        );

        if (user) {
            this.currentUser = { ...user };
            delete this.currentUser.password; // Não armazenar senha na sessão
            localStorage.setItem('currentUser', JSON.stringify(this.currentUser));
            return { success: true, user: this.currentUser };
        }

        return { success: false, message: 'Credenciais inválidas' };
    }

    loginDemo(role) {
        const user = this.users.find(u => u.role === role && u.active);
        if (user) {
            return this.login(user.email, user.password);
        }
        return { success: false, message: 'Usuário de demonstração não encontrado' };
    }

    logout() {
        this.currentUser = null;
        localStorage.removeItem('currentUser');
        window.location.href = '../index.html';
    }

    isAuthenticated() {
        return this.currentUser !== null;
    }

    getCurrentUser() {
        return this.currentUser;
    }

    hasPermission(permission) {
        if (!this.currentUser) return false;

        const permissions = {
            admin: ['all'],
            sindico: ['view_residents', 'manage_reservations', 'view_financial', 'manage_maintenance', 'view_security', 'manage_communication'],
            morador: ['view_own_data', 'make_reservations', 'view_own_financial', 'request_maintenance', 'view_communication'],
            porteiro: ['view_access_control', 'manage_visitors', 'view_security']
        };

        const userPermissions = permissions[this.currentUser.role] || [];
        return userPermissions.includes('all') || userPermissions.includes(permission);
    }

    updateProfile(userData) {
        if (!this.currentUser) return { success: false, message: 'Usuário não autenticado' };

        const userIndex = this.users.findIndex(u => u.id === this.currentUser.id);
        if (userIndex === -1) return { success: false, message: 'Usuário não encontrado' };

        // Atualizar dados do usuário
        this.users[userIndex] = { ...this.users[userIndex], ...userData };
        this.currentUser = { ...this.users[userIndex] };
        delete this.currentUser.password;

        this.saveUsers(this.users);
        localStorage.setItem('currentUser', JSON.stringify(this.currentUser));

        return { success: true, user: this.currentUser };
    }

    changePassword(currentPassword, newPassword) {
        if (!this.currentUser) return { success: false, message: 'Usuário não autenticado' };

        const user = this.users.find(u => u.id === this.currentUser.id);
        if (!user || user.password !== currentPassword) {
            return { success: false, message: 'Senha atual incorreta' };
        }

        user.password = newPassword;
        this.saveUsers(this.users);

        return { success: true, message: 'Senha alterada com sucesso' };
    }

    resetPassword(emailOrCpf) {
        const user = this.users.find(u => u.email === emailOrCpf || u.cpf === emailOrCpf);
        if (!user) {
            return { success: false, message: 'Usuário não encontrado' };
        }

        // Em um sistema real, enviaria email com link de reset
        // Para demonstração, apenas retorna sucesso
        return { 
            success: true, 
            message: 'Instruções de recuperação enviadas para seu email' 
        };
    }

    // Verificar se usuário deve ser redirecionado
    checkAuthRedirect() {
        const currentPage = window.location.pathname;
        const isLoginPage = currentPage.includes('index.html') || currentPage === '/';
        
        if (this.isAuthenticated() && isLoginPage) {
            window.location.href = 'pages/dashboard.html';
        } else if (!this.isAuthenticated() && !isLoginPage) {
            window.location.href = '../index.html';
        }
    }
}

// Instância global do sistema de autenticação
const auth = new AuthSystem();

// Verificar autenticação ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    auth.checkAuthRedirect();
});

// Função global para logout
function logout() {
    if (confirm('Tem certeza que deseja sair?')) {
        auth.logout();
    }
}

