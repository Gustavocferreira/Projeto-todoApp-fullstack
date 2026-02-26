Full-Stack To‑Do App (FastAPI + React + SQLAlchemy)
*Este projeto nasceu como um exercício de engenharia para demonstrar boas práticas em arquitetura desacoplada, infraestrutura conteinerizada e design sustentável de aplicações full‑stack.
Mais do que um simples “to‑do list”, o objetivo é mostrar como estruturar um sistema escalável e reproduzível, com separação clara entre responsabilidades e foco em DX (Developer Experience).*


⚡ Quick Start (Docker)
--
Todo o ecossistema — API, banco e frontend — é orquestrado via Docker Compose, garantindo isolamento total do ambiente e zero fricção na instalação.

bash
# Clone o repositório
git clone [(https://github.com/Gustavocferreira/Projeto-todoApp-fullstack)]
cd ProjetoTo-do

# Suba os containers
docker compose up --build
Frontend: http://localhost:5173

API Docs (Swagger): http://localhost:8000/docs

Health Check: curl http://localhost:8000/api/health

🧩 Visão de Arquitetura
--
A proposta é simples: uma aplicação moderna, modular e transparente na comunicação entre camadas.

Backend (FastAPI): Utiliza o modelo assíncrono do ASGI e validação baseada em type hints com Pydantic. O backend segue o princípio de Service Layer, onde as rotas expõem apenas a interface HTTP, e a lógica de negócio permanece isolada.

Acesso a Dados (SQLAlchemy ORM): A persistência é gerenciada pelo SQLAlchemy, atuando como o tradutor entre objetos Python e o banco relacional. O uso de Declarative Mapping garante que o esquema do banco seja tratado como código, protegendo a aplicação contra SQL Injection.
Evolução de Esquema (Alembic): O ciclo de vida do banco de dados é controlado via migrações versionadas.
Sincronização: Garante que todos os ambientes (Desenvolvimento, Docker e Produção) possuam exatamente a mesma estrutura de tabelas.
Rastreabilidade: Permite o rollback de alterações estruturais e mantém um histórico claro de como os dados evoluíram junto com as funcionalidades.

Frontend (React + Vite): O Vite foi escolhido pela velocidade de build e integração fluida com o React 18. As interações com a API são centralizadas em uma camada de abstração, garantindo consistência no tratamento de erros e autenticação.

Persistência (PostgreSQL): O banco é executado em container dedicado, com volumes persistentes e variáveis de ambiente gerenciadas. A prioridade é evitar dependências locais e manter o banco versionado de forma previsível entre ambientes.


Estrutura do Projeto
--
```
├── backend/            
│   ├── src/
│   │   ├── routes/      # Endpoints REST
│   │   ├── services/    # Lógica de negócio e integração com o BD
│   │   ├── models.py    # SQLAlchemy Models
│   │   └── schemas.py   # Pydantic Schemas (validação de dados)
├── frontend/            # SPA (React + Vite)
├── .devcontainer/       # Setup automatizado para VS Code Dev Containers
└── docker-compose.yml   # Orquestração completa dos serviços
```
💻 Desenvolvimento Local (Sem Docker)
Para cenários de debug manual ou execução parcial dos serviços, o projeto pode ser iniciado diretamente via Python e Node.

Backend
bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn src.main:app --reload
Frontend
bash
cd frontend
npm install
npm run dev

Apenas uma dica: Ajuste seu .env local para usar localhost em vez dos nomes de serviço Docker.
--

🔌 API Reference
--
Método	Endpoint	Descrição
GET	/api/tasks	Lista tarefas com ordenação por data
POST	/api/tasks	Cria nova tarefa (validação via Pydantic)
PUT	/api/tasks/{id}	Atualiza título ou status da tarefa
DELETE	/api/tasks/{id}	Remove o registro permanentemente
🧠 Boas Práticas e Convenções
O projeto adota princípios inspirados em plataformas de produção modernas:

Typing Estrito: Uso consistente de anotações de tipo, reduzindo erros em runtime e melhorando a DX.

Layered Architecture: Nenhuma rota tem acesso direto ao banco — o Service Layer abstrai toda a persistência.

Infraçao Reprodutível: Ambientes Dev e Prod utilizam a mesma base Docker/Compose.

Clean Commits e CI ready: Estrutura pronta para CI/CD (testes, lint e build automatizados).

🚀 Roadmap
--
 Migrações de schema com Alembic

 Testes de integração com Pytest + Testcontainers

 Autenticação e autorização via JWT

 Pipeline CI/CD (GitHub Actions) com steps para lint, teste e build

👤 Sobre Mim
--
Desenvolvido por Gustavo Costa Ferreira
Engenheiro focado em sistemas escaláveis, arquitetura limpa e automação de ambientes de desenvolvimento.
Este projeto reflete um princípio base: *“um bom código não precisa ser explicado — apenas reproduzido com confiança por qualquer membro do time.”*
