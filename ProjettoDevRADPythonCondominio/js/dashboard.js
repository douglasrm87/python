// Funcionalidades do Dashboard
document.addEventListener('DOMContentLoaded', function() {
    // Verificar autenticação
    if (!auth.isAuthenticated()) {
        window.location.href = '../index.html';
        return;
    }

    initializeDashboard();
    setupEventListeners();
    loadDashboardData();
});

function initializeDashboard() {
    const user = auth.getCurrentUser();
    
    // Atualizar informações do usuário na interface
    updateUserInfo(user);
    
    // Configurar sidebar baseado no papel do usuário
    setupSidebarForRole(user.role);
    
    // Carregar dados específicos do papel
    loadRoleSpecificData(user.role);
}

function updateUserInfo(user) {
    // Atualizar nome do usuário em vários locais
    const userNameElements = document.querySelectorAll('#userName, .user-name, #welcomeUserName');
    userNameElements.forEach(element => {
        if (element.id === 'welcomeUserName') {
            element.textContent = user.name.split(' ')[0]; // Apenas primeiro nome
        } else {
            element.textContent = user.name;
        }
    });
    
    // Atualizar papel do usuário
    const userRoleElements = document.querySelectorAll('#userRole, .user-role');
    userRoleElements.forEach(element => {
        element.textContent = getRoleDisplayName(user.role);
    });
}

function getRoleDisplayName(role) {
    const roleNames = {
        'morador': 'Morador',
        'sindico': 'Síndico',
        'admin': 'Administrador',
        'porteiro': 'Porteiro'
    };
    return roleNames[role] || role;
}

function setupSidebarForRole(role) {
    const navItems = document.querySelectorAll('.nav-item');
    
    // Definir quais itens cada papel pode ver
    const rolePermissions = {
        'morador': ['dashboard', 'reservas', 'financeiro', 'manutencao', 'comunicacao', 'configuracoes'],
        'sindico': ['dashboard', 'moradores', 'reservas', 'financeiro', 'manutencao', 'seguranca', 'comunicacao', 'configuracoes'],
        'admin': ['dashboard', 'moradores', 'reservas', 'financeiro', 'manutencao', 'seguranca', 'comunicacao', 'configuracoes'],
        'porteiro': ['dashboard', 'seguranca', 'comunicacao', 'configuracoes']
    };
    
    const allowedItems = rolePermissions[role] || [];
    
    navItems.forEach(item => {
        const link = item.querySelector('.nav-link');
        const href = link.getAttribute('href');
        const page = href.replace('.html', '');
        
        if (!allowedItems.includes(page)) {
            item.style.display = 'none';
        }
    });
}

function setupEventListeners() {
    // Toggle sidebar
    const sidebarToggle = document.getElementById('sidebarToggle');
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.querySelector('.main-content');
    
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', toggleSidebar);
    }
    
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', toggleMobileSidebar);
    }
    
    // Dropdown de notificações
    const notificationBtn = document.getElementById('notificationBtn');
    const notificationDropdown = document.getElementById('notificationDropdown');
    
    if (notificationBtn) {
        notificationBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            toggleDropdown(notificationDropdown);
        });
    }
    
    // Dropdown do usuário
    const userMenuBtn = document.getElementById('userMenuBtn');
    const userDropdown = document.getElementById('userDropdown');
    
    if (userMenuBtn) {
        userMenuBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            toggleDropdown(userDropdown);
        });
    }
    
    // Fechar dropdowns ao clicar fora
    document.addEventListener('click', function() {
        closeAllDropdowns();
    });
    
    // Marcar todas as notificações como lidas
    const markAllReadBtn = document.querySelector('.mark-all-read');
    if (markAllReadBtn) {
        markAllReadBtn.addEventListener('click', markAllNotificationsRead);
    }
    
    // Ações rápidas
    setupQuickActions();
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.querySelector('.main-content');
    
    sidebar.classList.toggle('collapsed');
    mainContent.classList.toggle('expanded');
}

function toggleMobileSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('show');
}

function toggleDropdown(dropdown) {
    if (dropdown) {
        dropdown.classList.toggle('show');
    }
}

function closeAllDropdowns() {
    const dropdowns = document.querySelectorAll('.notification-dropdown, .user-dropdown');
    dropdowns.forEach(dropdown => {
        dropdown.classList.remove('show');
    });
}

function markAllNotificationsRead() {
    const unreadNotifications = document.querySelectorAll('.notification-item.unread');
    unreadNotifications.forEach(notification => {
        notification.classList.remove('unread');
    });
    
    // Atualizar badge
    const badge = document.querySelector('.notification-badge');
    if (badge) {
        badge.textContent = '0';
        badge.style.display = 'none';
    }
    
    showToast('Todas as notificações foram marcadas como lidas', 'success');
}

function setupQuickActions() {
    const quickActionBtns = document.querySelectorAll('.quick-action-btn');
    
    quickActionBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const action = this.querySelector('span').textContent;
            handleQuickAction(action);
        });
    });
}

function handleQuickAction(action) {
    const user = auth.getCurrentUser();
    
    switch(action) {
        case 'Nova Reserva':
            if (auth.hasPermission('make_reservations')) {
                window.location.href = 'reservas.html';
            } else {
                showToast('Você não tem permissão para fazer reservas', 'warning');
            }
            break;
            
        case 'Manutenção':
            if (auth.hasPermission('request_maintenance')) {
                window.location.href = 'manutencao.html';
            } else {
                showToast('Você não tem permissão para solicitar manutenção', 'warning');
            }
            break;
            
        case 'Novo Morador':
            if (auth.hasPermission('manage_residents') || user.role === 'admin') {
                window.location.href = 'moradores.html';
            } else {
                showToast('Você não tem permissão para gerenciar moradores', 'warning');
            }
            break;
            
        case 'Novo Aviso':
            if (auth.hasPermission('manage_communication') || user.role === 'admin') {
                window.location.href = 'comunicacao.html';
            } else {
                showToast('Você não tem permissão para criar avisos', 'warning');
            }
            break;
            
        case 'Gerar Boleto':
            if (auth.hasPermission('view_financial')) {
                window.location.href = 'financeiro.html';
            } else {
                showToast('Você não tem permissão para acessar área financeira', 'warning');
            }
            break;
            
        case 'Relatórios':
            if (user.role === 'admin' || user.role === 'sindico') {
                showToast('Funcionalidade de relatórios em desenvolvimento', 'info');
            } else {
                showToast('Você não tem permissão para acessar relatórios', 'warning');
            }
            break;
            
        default:
            showToast('Funcionalidade em desenvolvimento', 'info');
    }
}

function loadDashboardData() {
    // Carregar estatísticas
    loadStatistics();
    
    // Carregar atividades recentes
    loadRecentActivities();
    
    // Carregar próximos eventos
    loadUpcomingEvents();
    
    // Carregar resumo financeiro
    loadFinancialSummary();
    
    // Atualizar clima
    updateWeather();
}

function loadRoleSpecificData(role) {
    // Carregar dados específicos baseado no papel do usuário
    switch(role) {
        case 'admin':
        case 'sindico':
            loadAdminData();
            break;
        case 'morador':
            loadResidentData();
            break;
        case 'porteiro':
            loadSecurityData();
            break;
    }
}

function loadStatistics() {
    // Simular carregamento de estatísticas
    const stats = {
        totalUnits: 150,
        activeResidents: 320,
        monthlyRevenue: 12500,
        openRequests: 15
    };
    
    // Atualizar cards de estatísticas
    updateStatCard('.stat-card:nth-child(1) h3', stats.totalUnits);
    updateStatCard('.stat-card:nth-child(2) h3', stats.activeResidents);
    updateStatCard('.stat-card:nth-child(3) h3', `R$ ${stats.monthlyRevenue.toLocaleString()}`);
    updateStatCard('.stat-card:nth-child(4) h3', stats.openRequests);
}

function updateStatCard(selector, value) {
    const element = document.querySelector(selector);
    if (element) {
        element.textContent = value;
    }
}

function loadRecentActivities() {
    const activities = [
        {
            icon: 'fa-calendar-check',
            iconClass: 'text-success',
            text: '<strong>Maria Santos</strong> reservou a churrasqueira',
            time: 'Há 30 minutos'
        },
        {
            icon: 'fa-tools',
            iconClass: 'text-warning',
            text: '<strong>Carlos Lima</strong> solicitou manutenção no elevador',
            time: 'Há 1 hora'
        },
        {
            icon: 'fa-dollar-sign',
            iconClass: 'text-success',
            text: '<strong>Ana Costa</strong> efetuou pagamento da taxa',
            time: 'Há 2 horas'
        },
        {
            icon: 'fa-user-plus',
            iconClass: 'text-info',
            text: '<strong>Pedro Oliveira</strong> foi cadastrado como novo morador',
            time: 'Há 3 horas'
        }
    ];
    
    const activityList = document.querySelector('.activity-list');
    if (activityList) {
        activityList.innerHTML = activities.map(activity => `
            <div class="activity-item">
                <div class="activity-icon">
                    <i class="fas ${activity.icon} ${activity.iconClass}"></i>
                </div>
                <div class="activity-content">
                    <p>${activity.text}</p>
                    <small>${activity.time}</small>
                </div>
            </div>
        `).join('');
    }
}

function loadUpcomingEvents() {
    const events = [
        {
            day: '15',
            month: 'JUL',
            title: 'Assembleia Geral',
            description: 'Discussão sobre melhorias no condomínio',
            time: '19:00'
        },
        {
            day: '18',
            month: 'JUL',
            title: 'Manutenção Preventiva',
            description: 'Limpeza da caixa d\'água',
            time: '08:00'
        },
        {
            day: '22',
            month: 'JUL',
            title: 'Festa Julina',
            description: 'Confraternização dos moradores',
            time: '18:00'
        }
    ];
    
    const eventsList = document.querySelector('.events-list');
    if (eventsList) {
        eventsList.innerHTML = events.map(event => `
            <div class="event-item">
                <div class="event-date">
                    <span class="day">${event.day}</span>
                    <span class="month">${event.month}</span>
                </div>
                <div class="event-content">
                    <h4>${event.title}</h4>
                    <p>${event.description}</p>
                    <small><i class="fas fa-clock"></i> ${event.time}</small>
                </div>
            </div>
        `).join('');
    }
}

function loadFinancialSummary() {
    const financial = {
        revenue: 45200,
        expenses: 32800,
        balance: 12400
    };
    
    // Atualizar valores financeiros
    const revenueElement = document.querySelector('.financial-item:nth-child(1) .financial-value');
    const expensesElement = document.querySelector('.financial-item:nth-child(2) .financial-value');
    const balanceElement = document.querySelector('.financial-item:nth-child(3) .financial-value');
    
    if (revenueElement) revenueElement.textContent = `R$ ${financial.revenue.toLocaleString()}`;
    if (expensesElement) expensesElement.textContent = `R$ ${financial.expenses.toLocaleString()}`;
    if (balanceElement) balanceElement.textContent = `R$ ${financial.balance.toLocaleString()}`;
}

function loadAdminData() {
    // Dados específicos para admin/síndico
    console.log('Carregando dados administrativos...');
}

function loadResidentData() {
    // Dados específicos para morador
    console.log('Carregando dados do morador...');
}

function loadSecurityData() {
    // Dados específicos para porteiro
    console.log('Carregando dados de segurança...');
}

function updateWeather() {
    // Simular atualização do clima
    const weatherWidget = document.querySelector('.weather-widget span');
    if (weatherWidget) {
        const temp = Math.floor(Math.random() * 10) + 20; // 20-30°C
        weatherWidget.textContent = `${temp}°C`;
    }
}

// Função para mostrar toast
function showToast(message, type = 'info') {
    const existingToast = document.querySelector('.toast');
    if (existingToast) {
        existingToast.remove();
    }

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <div style="display: flex; align-items: center; gap: 8px;">
            <i class="fas ${getToastIcon(type)}"></i>
            <span>${message}</span>
        </div>
    `;

    document.body.appendChild(toast);

    setTimeout(() => {
        toast.classList.add('show');
    }, 100);

    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => {
            if (toast.parentNode) {
                toast.remove();
            }
        }, 300);
    }, 5000);
}

function getToastIcon(type) {
    const icons = {
        success: 'fa-check-circle',
        error: 'fa-exclamation-circle',
        warning: 'fa-exclamation-triangle',
        info: 'fa-info-circle'
    };
    return icons[type] || icons.info;
}

