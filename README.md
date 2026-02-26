📝 Full-Stack To‑Do App (FastAPI + React)Este projeto nasceu como um exercício de engenharia para demonstrar boas práticas em arquitetura desacoplada, infraestrutura conteinerizada e design sustentável de aplicações full‑stack.Mais do que um simples "to‑do list", o objetivo é mostrar como estruturar um sistema escalável e reproduzível, com separação clara entre responsabilidades e foco total em DX (Developer Experience).⚡ Quick Start (Docker)Todo o ecossistema — API, banco e frontend — é orquestrado via Docker Compose, garantindo isolamento total do ambiente e zero fricção na instalação.Bash# 1. Clone o repositório
git clone https://github.com/Gustavocferreira/Projeto-todoApp-fullstack
cd Projeto-todoApp-fullstack

# 2. Suba os containers
docker compose up --build
Frontend: http://localhost:5173API Docs (Swagger): http://localhost:8000/docsHealth Check: curl http://localhost:8000/api/health🧩 Visão de ArquiteturaA proposta é simples: uma aplicação moderna, modular e transparente na comunicação entre camadas.Backend (FastAPI): Utiliza o modelo assíncrono do ASGI e validação baseada em type hints com Pydantic. Segue o princípio de Service Layer, onde as rotas expõem apenas a interface HTTP, e a lógica de negócio permanece isolada.Acesso a Dados (SQLAlchemy & Alembic): A persistência é gerenciada via ORM, garantindo que o esquema do banco seja tratado como código. O Alembic controla o ciclo de vida do banco através de migrações versionadas, garantindo consistência entre ambientes.Frontend (React + Vite): O Vite foi escolhido pela velocidade de build e integração fluida com o React 18. As interações com a API são centralizadas em uma camada de abstração (Axios/Services), garantindo consistência no tratamento de erros.Persistência (PostgreSQL): Executado em container dedicado, com volumes persistentes. A prioridade é evitar dependências locais e manter o banco versionado de forma previsível.Fluxo de DadosSnippet de códigograph TD
    A[Frontend - React/Vite] <-->|JSON/HTTP| B[FastAPI - Router]
    B <--> C[Service Layer - Business Logic]
    C <--> D[SQLAlchemy - ORM]
    D <--> E[(PostgreSQL)]
    F[Alembic - Migrations] -.->|Evolução de Esquema| E
📂 Estrutura do ProjetoPlaintext.
├── backend/
│   ├── src/
│   │   ├── routes/      # Endpoints REST (O Recepcionista)
│   │   ├── services/    # Lógica de negócio (A Cozinha)
│   │   ├── models.py    # SQLAlchemy Models (O Banco)
│   │   └── schemas.py   # Pydantic Schemas (A Validação)
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/            # SPA (React + Vite)
├── .devcontainer/       # Setup para VS Code Dev Containers
└── docker-compose.yml   # Orquestração completa dos serviços
🔌 API ReferenceMétodoEndpointDescriçãoGET/api/tasksLista tarefas com ordenação por data.POST/api/tasksCria nova tarefa (validação via Pydantic).PUT/api/tasks/{id}Atualiza título, status ou data de vencimento.DELETE/api/tasks/{id}Remove o registro permanentemente.🧠 Boas Práticas e ConvençõesO projeto adota princípios inspirados em plataformas de produção modernas:Typing Estrito: Uso consistente de anotações de tipo, reduzindo erros em runtime.Layered Architecture: Nenhuma rota tem acesso direto ao banco — o Service Layer abstrai a persistência.Infraestrutura Reprodutível: Ambientes de Desenvolvimento e Produção utilizam a mesma base Docker.🚀 Roadmap de Evolução[x] Arquitetura Base e Dockerização[ ] Migrações de schema com Alembic[ ] Autenticação e autorização via JWT[ ] Sistema de Gamificação (XP e Level Up por Task)[ ] Pipeline CI/CD (GitHub Actions)👤 Sobre o AutorGustavo Costa Ferreira Full-stack Developer & DevOps no Instituto do Legislativo Paulista (Alesp).Focado em sistemas escaláveis, arquitetura limpa e automação de ambientes."Um bom código não precisa ser explicado — apenas reproduzido com confiança por qualquer membro do time."
