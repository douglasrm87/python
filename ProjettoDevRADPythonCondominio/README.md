# Smart Condo - Sistema de Gestão Condominial

## 📋 Sobre o Projeto

O Smart Condo é um sistema completo de gestão condominial desenvolvido com tecnologias web modernas (HTML5, CSS3 e JavaScript). O sistema oferece uma interface intuitiva e responsiva para facilitar a administração de condomínios residenciais.

## 🎯 Objetivos

- Digitalizar processos administrativos do condomínio
- Facilitar a comunicação entre moradores e administração
- Automatizar controle de acesso e segurança
- Gerenciar reservas de áreas comuns
- Controlar finanças e taxas condominiais
- Melhorar a experiência dos moradores

## 🚀 Funcionalidades Principais

### 🔐 Sistema de Autenticação
- Login seguro com diferentes níveis de acesso
- Perfis de usuário: Morador, Síndico, Administrador, Porteiro
- Recuperação de senha
- Contas de demonstração para testes

### 📊 Dashboard Inteligente
- Visão geral personalizada por tipo de usuário
- Estatísticas em tempo real
- Notificações importantes
- Ações rápidas
- Atividades recentes
- Próximos eventos

### 👥 Gestão de Moradores
- Cadastro e edição de dados dos moradores
- Controle de unidades habitacionais
- Histórico de ocorrências
- Documentos pessoais

### 🏢 Reservas de Áreas Comuns
- Sistema de reservas online
- Calendário de disponibilidade
- Controle de horários e regras
- Gestão de equipamentos

### 💰 Gestão Financeira
- Controle de taxas condominiais
- Histórico de pagamentos
- Relatórios financeiros
- Gestão de inadimplência

### 🔧 Manutenção
- Sistema de solicitação de manutenção
- Acompanhamento de status
- Histórico de serviços
- Avaliação de prestadores

### 🛡️ Segurança
- Central de monitoramento
- Registro de ocorrências
- Controle de acesso
- Relatórios de segurança

### 📢 Comunicação
- Mural de avisos digital
- Sistema de mensagens internas
- Notificações push
- Enquetes e votações

## 🛠️ Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Armazenamento**: LocalStorage para persistência local
- **Design**: Responsive Design, Mobile First
- **Ícones**: Font Awesome 6.0
- **Tipografia**: Inter Font Family

## 📁 Estrutura do Projeto

```
condominio-inteligente/
├── index.html                 # Página de login
├── css/
│   ├── style.css             # Estilos principais
│   ├── login.css             # Estilos da página de login
│   └── dashboard.css         # Estilos do dashboard
├── js/
│   ├── auth.js               # Sistema de autenticação
│   ├── login.js              # Funcionalidades de login
│   ├── dashboard.js          # Funcionalidades do dashboard
│   └── utils.js              # Utilitários JavaScript
├── images/
│   ├── logo_condominio.png   # Logo do sistema
│   ├── dashboard_mockup.png  # Mockup do dashboard
│   └── mobile_interface.png  # Interface mobile
├── pages/
│   ├── dashboard.html        # Dashboard principal
│   └── reservas.html         # Página de reservas
├── data/
│   └── mock-data.js          # Dados de demonstração
└── README.md                 # Documentação do projeto
```

## 🎨 Design System

### Paleta de Cores
- **Azul Principal**: #2563EB
- **Azul Escuro**: #1E40AF
- **Verde Tecnológico**: #10B981
- **Verde Claro**: #34D399
- **Branco**: #FFFFFF
- **Cinza Claro**: #F8FAFC
- **Cinza Médio**: #64748B
- **Cinza Escuro**: #334155

### Tipografia
- **Fonte Principal**: Inter, Segoe UI, Roboto, sans-serif
- **H1**: 2.5rem (40px), font-weight: 700
- **H2**: 2rem (32px), font-weight: 600
- **H3**: 1.5rem (24px), font-weight: 600
- **Body**: 1rem (16px), font-weight: 400

## 🚀 Como Executar

1. **Clone ou baixe o projeto**
   ```bash
   git clone [url-do-repositorio]
   cd condominio-inteligente
   ```

2. **Inicie um servidor local**
   ```bash
   # Usando Python
   python -m http.server 8080
   
   # Ou usando Node.js
   npx http-server -p 8080
   ```

3. **Acesse o sistema**
   - Abra o navegador e vá para: `http://localhost:8080`

## 👤 Contas de Demonstração

O sistema inclui contas pré-configuradas para teste:

### Morador
- **Email**: morador@smartcondo.com
- **Senha**: 123456
- **Acesso**: Dashboard, Reservas, Financeiro, Manutenção, Comunicação

### Síndico
- **Email**: sindico@smartcondo.com
- **Senha**: 123456
- **Acesso**: Todas as funcionalidades exceto administração completa

### Administrador
- **Email**: admin@smartcondo.com
- **Senha**: 123456
- **Acesso**: Todas as funcionalidades do sistema

### Porteiro
- **Email**: porteiro@smartcondo.com
- **Senha**: 123456
- **Acesso**: Segurança, Controle de Acesso, Comunicação

## 📱 Responsividade

O sistema foi desenvolvido com abordagem Mobile First e é totalmente responsivo:

- **Desktop**: 1024px+
- **Tablet**: 768px - 1024px
- **Mobile**: 320px - 768px

## 🔧 Funcionalidades Implementadas

### ✅ Completas
- [x] Sistema de autenticação
- [x] Dashboard interativo
- [x] Design responsivo
- [x] Navegação entre páginas
- [x] Sistema de notificações
- [x] Persistência de dados local
- [x] Diferentes perfis de usuário

### 🚧 Em Desenvolvimento
- [ ] Módulo de reservas completo
- [ ] Gestão financeira detalhada
- [ ] Sistema de manutenção
- [ ] Central de segurança
- [ ] Comunicação interna

## 🎯 Casos de Uso

### UC001 - Login no Sistema
1. Usuário acessa a página de login
2. Insere credenciais ou usa conta demo
3. Sistema valida e redireciona para dashboard

### UC002 - Visualizar Dashboard
1. Usuário logado acessa dashboard
2. Visualiza estatísticas personalizadas
3. Acessa ações rápidas e notificações

### UC003 - Navegar pelo Sistema
1. Usuário utiliza sidebar para navegação
2. Acessa diferentes módulos conforme permissões
3. Mantém sessão ativa durante navegação

## 🔒 Segurança

- Validação de credenciais
- Controle de acesso baseado em perfis
- Proteção contra acesso não autorizado
- Sessões seguras com localStorage

## 📊 Performance

- Carregamento rápido das páginas
- Animações suaves e responsivas
- Otimização de imagens
- Código JavaScript modular

## 🌐 Compatibilidade

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais como projeto de faculdade.

## 👨‍💻 Desenvolvimento

Desenvolvido utilizando as melhores práticas de desenvolvimento web:

- Código limpo e bem documentado
- Arquitetura modular
- Separação de responsabilidades
- Padrões de design modernos
- Acessibilidade web

## 🚀 Próximos Passos

1. Implementação completa dos módulos restantes
2. Integração com backend real
3. Sistema de notificações em tempo real
4. Aplicativo mobile nativo
5. Relatórios avançados e analytics

---

**Smart Condo** - Transformando a gestão condominial através da tecnologia! 🏢✨

