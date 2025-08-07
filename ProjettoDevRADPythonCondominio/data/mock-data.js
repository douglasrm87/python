// Dados de demonstração para o sistema
const MockData = {
    // Dados dos moradores
    residents: [
        {
            id: 1,
            name: 'João Silva',
            email: 'joao.silva@email.com',
            cpf: '123.456.789-00',
            phone: '(11) 99999-9999',
            apartment: '101',
            block: 'A',
            role: 'morador',
            active: true,
            moveInDate: '2023-01-15',
            emergencyContact: {
                name: 'Maria Silva',
                phone: '(11) 88888-8888',
                relationship: 'Esposa'
            },
            vehicles: [
                {
                    plate: 'ABC-1234',
                    model: 'Honda Civic',
                    color: 'Prata'
                }
            ]
        },
        {
            id: 2,
            name: 'Maria Santos',
            email: 'maria.santos@email.com',
            cpf: '987.654.321-00',
            phone: '(11) 88888-8888',
            apartment: '205',
            block: 'B',
            role: 'sindico',
            active: true,
            moveInDate: '2022-06-10',
            emergencyContact: {
                name: 'José Santos',
                phone: '(11) 77777-7777',
                relationship: 'Marido'
            },
            vehicles: [
                {
                    plate: 'XYZ-5678',
                    model: 'Toyota Corolla',
                    color: 'Branco'
                }
            ]
        },
        {
            id: 3,
            name: 'Carlos Lima',
            email: 'carlos.lima@email.com',
            cpf: '456.789.123-00',
            phone: '(11) 77777-7777',
            apartment: '302',
            block: 'A',
            role: 'morador',
            active: true,
            moveInDate: '2023-03-20',
            emergencyContact: {
                name: 'Ana Lima',
                phone: '(11) 66666-6666',
                relationship: 'Esposa'
            },
            vehicles: []
        }
    ],

    // Dados de reservas
    reservations: [
        {
            id: 1,
            residentId: 1,
            residentName: 'João Silva',
            area: 'Churrasqueira 1',
            date: '2024-08-15',
            startTime: '18:00',
            endTime: '22:00',
            status: 'confirmada',
            guests: 8,
            observations: 'Aniversário de casamento',
            createdAt: '2024-07-30T10:00:00Z'
        },
        {
            id: 2,
            residentId: 2,
            residentName: 'Maria Santos',
            area: 'Salão de Festas',
            date: '2024-08-20',
            startTime: '19:00',
            endTime: '23:00',
            status: 'pendente',
            guests: 25,
            observations: 'Festa de formatura',
            createdAt: '2024-07-29T14:30:00Z'
        },
        {
            id: 3,
            residentId: 3,
            residentName: 'Carlos Lima',
            area: 'Quadra Esportiva',
            date: '2024-08-10',
            startTime: '08:00',
            endTime: '10:00',
            status: 'concluida',
            guests: 4,
            observations: 'Jogo de futebol',
            createdAt: '2024-07-25T09:15:00Z'
        }
    ],

    // Áreas comuns disponíveis
    commonAreas: [
        {
            id: 1,
            name: 'Churrasqueira 1',
            capacity: 12,
            hourlyRate: 50,
            availableHours: ['18:00', '19:00', '20:00', '21:00', '22:00'],
            equipment: ['Churrasqueira', 'Mesas', 'Cadeiras', 'Pia'],
            rules: [
                'Limpeza obrigatória após o uso',
                'Máximo 12 pessoas',
                'Não é permitido som alto após 22h'
            ]
        },
        {
            id: 2,
            name: 'Churrasqueira 2',
            capacity: 8,
            hourlyRate: 40,
            availableHours: ['18:00', '19:00', '20:00', '21:00', '22:00'],
            equipment: ['Churrasqueira', 'Mesas', 'Cadeiras'],
            rules: [
                'Limpeza obrigatória após o uso',
                'Máximo 8 pessoas',
                'Não é permitido som alto após 22h'
            ]
        },
        {
            id: 3,
            name: 'Salão de Festas',
            capacity: 50,
            hourlyRate: 150,
            availableHours: ['19:00', '20:00', '21:00', '22:00', '23:00'],
            equipment: ['Som', 'Iluminação', 'Mesas', 'Cadeiras', 'Cozinha'],
            rules: [
                'Reserva com 15 dias de antecedência',
                'Limpeza profissional obrigatória',
                'Caução de R$ 500,00'
            ]
        },
        {
            id: 4,
            name: 'Quadra Esportiva',
            capacity: 20,
            hourlyRate: 30,
            availableHours: ['06:00', '07:00', '08:00', '09:00', '18:00', '19:00', '20:00', '21:00'],
            equipment: ['Traves', 'Cestas', 'Rede de vôlei'],
            rules: [
                'Uso de tênis obrigatório',
                'Máximo 2 horas por reserva',
                'Não é permitido após 22h'
            ]
        },
        {
            id: 5,
            name: 'Piscina',
            capacity: 30,
            hourlyRate: 0,
            availableHours: ['06:00', '07:00', '08:00', '09:00', '10:00', '14:00', '15:00', '16:00', '17:00', '18:00'],
            equipment: ['Cadeiras', 'Guarda-sol', 'Chuveiros'],
            rules: [
                'Uso de touca obrigatório',
                'Crianças devem estar acompanhadas',
                'Não é permitido comida na área da piscina'
            ]
        }
    ],

    // Dados financeiros
    financial: [
        {
            id: 1,
            residentId: 1,
            residentName: 'João Silva',
            apartment: '101',
            month: '2024-07',
            condominiumFee: 450.00,
            waterBill: 85.30,
            extraCharges: 0,
            total: 535.30,
            dueDate: '2024-07-10',
            paidDate: '2024-07-08',
            status: 'pago',
            paymentMethod: 'PIX'
        },
        {
            id: 2,
            residentId: 2,
            residentName: 'Maria Santos',
            apartment: '205',
            month: '2024-07',
            condominiumFee: 520.00,
            waterBill: 92.15,
            extraCharges: 50.00,
            total: 662.15,
            dueDate: '2024-07-10',
            paidDate: '2024-07-09',
            status: 'pago',
            paymentMethod: 'Boleto'
        },
        {
            id: 3,
            residentId: 3,
            residentName: 'Carlos Lima',
            apartment: '302',
            month: '2024-07',
            condominiumFee: 480.00,
            waterBill: 78.45,
            extraCharges: 0,
            total: 558.45,
            dueDate: '2024-07-10',
            paidDate: null,
            status: 'pendente',
            paymentMethod: null
        }
    ],

    // Solicitações de manutenção
    maintenanceRequests: [
        {
            id: 1,
            residentId: 1,
            residentName: 'João Silva',
            apartment: '101',
            category: 'Elétrica',
            priority: 'alta',
            title: 'Tomada sem energia na cozinha',
            description: 'A tomada próxima à pia da cozinha não está funcionando. Já verifiquei o disjuntor.',
            status: 'em_andamento',
            createdAt: '2024-07-28T14:30:00Z',
            assignedTo: 'João Eletricista',
            estimatedCompletion: '2024-07-31',
            photos: []
        },
        {
            id: 2,
            residentId: 2,
            residentName: 'Maria Santos',
            apartment: '205',
            category: 'Hidráulica',
            priority: 'media',
            title: 'Vazamento no banheiro',
            description: 'Pequeno vazamento na válvula de descarga do banheiro social.',
            status: 'pendente',
            createdAt: '2024-07-29T09:15:00Z',
            assignedTo: null,
            estimatedCompletion: null,
            photos: []
        },
        {
            id: 3,
            residentId: 3,
            residentName: 'Carlos Lima',
            apartment: '302',
            category: 'Geral',
            priority: 'baixa',
            title: 'Porta do armário descascando',
            description: 'A tinta da porta do armário da cozinha está descascando.',
            status: 'concluida',
            createdAt: '2024-07-20T16:45:00Z',
            assignedTo: 'Pedro Pintor',
            estimatedCompletion: '2024-07-25',
            completedAt: '2024-07-24T10:00:00Z',
            photos: []
        }
    ],

    // Ocorrências de segurança
    securityIncidents: [
        {
            id: 1,
            type: 'Visitante não autorizado',
            description: 'Pessoa tentou entrar sem autorização do morador',
            severity: 'media',
            location: 'Portaria principal',
            reportedBy: 'Pedro Porteiro',
            reportedAt: '2024-07-29T22:30:00Z',
            status: 'resolvida',
            actions: 'Pessoa foi orientada sobre o procedimento correto'
        },
        {
            id: 2,
            type: 'Barulho excessivo',
            description: 'Música alta após horário permitido',
            severity: 'baixa',
            location: 'Apartamento 305',
            reportedBy: 'Morador Anônimo',
            reportedAt: '2024-07-28T23:45:00Z',
            status: 'em_andamento',
            actions: 'Síndico foi notificado'
        }
    ],

    // Comunicados e avisos
    communications: [
        {
            id: 1,
            title: 'Assembleia Geral Ordinária',
            content: 'Convocamos todos os condôminos para a Assembleia Geral Ordinária que será realizada no dia 15 de agosto de 2024, às 19h, no salão de festas.',
            type: 'assembleia',
            priority: 'alta',
            author: 'Maria Santos',
            authorRole: 'Síndico',
            publishedAt: '2024-07-25T10:00:00Z',
            expiresAt: '2024-08-15T19:00:00Z',
            attachments: []
        },
        {
            id: 2,
            title: 'Manutenção do Elevador',
            content: 'Informamos que será realizada manutenção preventiva no elevador do Bloco A no dia 18 de julho, das 8h às 17h.',
            type: 'manutencao',
            priority: 'media',
            author: 'Administração',
            authorRole: 'Admin',
            publishedAt: '2024-07-15T14:30:00Z',
            expiresAt: '2024-07-18T17:00:00Z',
            attachments: []
        },
        {
            id: 3,
            title: 'Nova regra para uso da piscina',
            content: 'A partir de 1º de agosto, o uso da piscina será limitado a 2 horas por família por dia, para garantir que todos possam aproveitar.',
            type: 'regras',
            priority: 'media',
            author: 'Maria Santos',
            authorRole: 'Síndico',
            publishedAt: '2024-07-20T16:00:00Z',
            expiresAt: null,
            attachments: []
        }
    ],

    // Controle de acesso
    accessControl: [
        {
            id: 1,
            type: 'entrada',
            personName: 'João Silva',
            personType: 'morador',
            apartment: '101',
            timestamp: '2024-07-30T08:30:00Z',
            authorizedBy: 'Próprio morador',
            notes: ''
        },
        {
            id: 2,
            type: 'entrada',
            personName: 'Ana Costa',
            personType: 'visitante',
            apartment: '205',
            timestamp: '2024-07-30T14:15:00Z',
            authorizedBy: 'Maria Santos',
            notes: 'Entrega de encomenda'
        },
        {
            id: 3,
            type: 'saida',
            personName: 'Carlos Lima',
            personType: 'morador',
            apartment: '302',
            timestamp: '2024-07-30T07:45:00Z',
            authorizedBy: 'Próprio morador',
            notes: ''
        }
    ],

    // Fornecedores e prestadores de serviço
    serviceProviders: [
        {
            id: 1,
            name: 'João Eletricista',
            category: 'Elétrica',
            phone: '(11) 99999-1111',
            email: 'joao.eletricista@email.com',
            rating: 4.8,
            active: true
        },
        {
            id: 2,
            name: 'Pedro Pintor',
            category: 'Pintura',
            phone: '(11) 99999-2222',
            email: 'pedro.pintor@email.com',
            rating: 4.5,
            active: true
        },
        {
            id: 3,
            name: 'Maria Limpeza',
            category: 'Limpeza',
            phone: '(11) 99999-3333',
            email: 'maria.limpeza@email.com',
            rating: 4.9,
            active: true
        }
    ],

    // Configurações do sistema
    settings: {
        condominium: {
            name: 'Residencial Smart Condo',
            address: 'Rua das Flores, 123 - Jardim Primavera',
            city: 'São Paulo',
            state: 'SP',
            zipCode: '01234-567',
            phone: '(11) 3333-4444',
            email: 'contato@smartcondo.com.br',
            cnpj: '12.345.678/0001-90'
        },
        features: {
            reservations: true,
            financial: true,
            maintenance: true,
            security: true,
            communications: true,
            accessControl: true
        },
        notifications: {
            email: true,
            sms: false,
            push: true
        }
    }
};

// Funções para manipular os dados
const DataManager = {
    // Salvar dados no localStorage
    saveData() {
        Object.keys(MockData).forEach(key => {
            localStorage.setItem(`smartcondo_${key}`, JSON.stringify(MockData[key]));
        });
    },

    // Carregar dados do localStorage
    loadData() {
        Object.keys(MockData).forEach(key => {
            const saved = localStorage.getItem(`smartcondo_${key}`);
            if (saved) {
                MockData[key] = JSON.parse(saved);
            }
        });
    },

    // Inicializar dados se não existirem
    initializeData() {
        const hasData = localStorage.getItem('smartcondo_residents');
        if (!hasData) {
            this.saveData();
        } else {
            this.loadData();
        }
    },

    // Obter dados por categoria
    getData(category) {
        return MockData[category] || [];
    },

    // Adicionar item
    addItem(category, item) {
        if (!MockData[category]) {
            MockData[category] = [];
        }
        
        item.id = this.generateId();
        MockData[category].push(item);
        this.saveCategory(category);
        return item;
    },

    // Atualizar item
    updateItem(category, id, updates) {
        const items = MockData[category];
        const index = items.findIndex(item => item.id == id);
        
        if (index !== -1) {
            MockData[category][index] = { ...items[index], ...updates };
            this.saveCategory(category);
            return MockData[category][index];
        }
        
        return null;
    },

    // Remover item
    removeItem(category, id) {
        const items = MockData[category];
        const index = items.findIndex(item => item.id == id);
        
        if (index !== -1) {
            const removed = items.splice(index, 1)[0];
            this.saveCategory(category);
            return removed;
        }
        
        return null;
    },

    // Salvar categoria específica
    saveCategory(category) {
        localStorage.setItem(`smartcondo_${category}`, JSON.stringify(MockData[category]));
    },

    // Gerar ID único
    generateId() {
        return Date.now() + Math.random().toString(36).substr(2, 9);
    },

    // Filtrar dados
    filter(category, filterFn) {
        return MockData[category].filter(filterFn);
    },

    // Buscar por ID
    findById(category, id) {
        return MockData[category].find(item => item.id == id);
    }
};

// Inicializar dados ao carregar
document.addEventListener('DOMContentLoaded', () => {
    DataManager.initializeData();
});

// Exportar para uso global
window.MockData = MockData;
window.DataManager = DataManager;

