# 📝 To-Do App Full-Stack

Aplicação completa de gerenciamento de tarefas (To-Do) construída com FastAPI (Python), React + Vite e PostgreSQL, totalmente containerizada com Docker.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green)
![React](https://img.shields.io/badge/React-18.2-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)

## 🎯 Objetivo

Projeto de portfólio demonstrando uma arquitetura full-stack moderna com:
- ✅ Backend RESTful em Python/FastAPI
- ✅ Frontend moderno em React + Vite
- ✅ Banco de dados PostgreSQL persistente
- ✅ Containerização completa com Docker
- ✅ Ambiente de desenvolvimento isolado (Dev Container)
- ✅ Código limpo e bem documentado

---

## 🏗️ Arquitetura

```
ProjetoTo-do/
├── backend/                 # API FastAPI
│   ├── src/
│   │   ├── main.py         # Bootstrap da aplicação
│   │   ├── database.py     # Configuração do SQLAlchemy
│   │   ├── models.py       # Modelos do banco de dados
│   │   ├── schemas.py      # Schemas Pydantic
│   │   ├── routes/         # Rotas da API
│   │   │   └── tasks.py
│   │   └── services/       # Lógica de negócio
│   │       └── task_service.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/               # Aplicação React
│   ├── src/
│   │   ├── App.jsx        # Componente principal
│   │   ├── App.css        # Estilos
│   │   └── main.jsx       # Entry point
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── Dockerfile
│
├── .devcontainer/         # Configuração Dev Container
│   └── devcontainer.json
│
└── docker-compose.yml     # Orquestração dos serviços
```

---

## 🚀 Tecnologias

### Backend
- **FastAPI** - Framework web moderno e rápido para APIs
- **SQLAlchemy** - ORM para Python
- **PostgreSQL** - Banco de dados relacional
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI

### Frontend
- **React 18** - Biblioteca para interfaces de usuário
- **Vite** - Build tool super rápida
- **CSS moderno** - Estilização responsiva

### DevOps
- **Docker & Docker Compose** - Containerização
- **Dev Containers** - Ambiente de desenvolvimento isolado

---

## 📋 Funcionalidades

### API (Backend)
- ✅ **GET** `/api/health` - Health check
- ✅ **GET** `/api/tasks` - Listar todas as tarefas
- ✅ **POST** `/api/tasks` - Criar nova tarefa
- ✅ **PUT** `/api/tasks/:id` - Atualizar tarefa
- ✅ **DELETE** `/api/tasks/:id` - Deletar tarefa

### Interface (Frontend)
- ✅ Adicionar novas tarefas
- ✅ Listar tarefas ordenadas por data de criação
- ✅ Marcar/desmarcar tarefas como concluídas
- ✅ Excluir tarefas
- ✅ Visualizar estatísticas (total, concluídas, pendentes)
- ✅ Interface responsiva e moderna

### Validações
- ✅ Título obrigatório (3-80 caracteres)
- ✅ Título não pode ser vazio ou apenas espaços
- ✅ Tratamento de erros da API
- ✅ Feedback visual ao usuário

---

## 🔧 Pré-requisitos

- **Docker** (versão 20.10 ou superior)
- **Docker Compose** (versão 2.0 ou superior)

**OU**

- **VS Code** com extensão **Dev Containers** (recomendado)

---

## 🏃 Como Executar

### Opção 1: Docker Compose (Recomendado)

1. **Clone o repositório** (se ainda não o fez):
```bash
git clone <seu-repositorio>
cd ProjetoTo-do
```

2. **Inicie todos os serviços**:
```bash
docker compose up --build
```

3. **Aguarde** a inicialização (pode levar alguns minutos na primeira vez)

4. **Acesse a aplicação**:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - Documentação API (Swagger): http://localhost:8000/docs

5. **Para parar os serviços**:
```bash
# Ctrl+C no terminal
# Ou em outro terminal:
docker compose down
```

### Opção 2: Dev Container (VS Code)

1. **Abra o projeto no VS Code**

2. **Instale a extensão**: `ms-vscode-remote.remote-containers`

3. **Abra a Command Palette** (`Ctrl+Shift+P` / `Cmd+Shift+P`)

4. **Execute**: `Dev Containers: Reopen in Container`

5. **Aguarde** a construção do ambiente (primeira vez demora mais)

6. **Use o terminal integrado** para executar comandos dentro do container

---

## 🧪 Testando a API

### Usando curl:

```bash
# Health check
curl http://localhost:8000/api/health

# Listar tarefas
curl http://localhost:8000/api/tasks

# Criar tarefa
curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Minha primeira tarefa"}'

# Atualizar tarefa (ID 1)
curl -X PUT http://localhost:8000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'

# Deletar tarefa (ID 1)
curl -X DELETE http://localhost:8000/api/tasks/1
```

### Usando a interface Swagger:
Acesse: http://localhost:8000/docs

---

## 🗄️ Persistência de Dados

Os dados são armazenados em um volume Docker nomeado `postgres_data`, garantindo que:
- ✅ Dados **não são perdidos** ao reiniciar os containers
- ✅ Dados **não são perdidos** ao recriar os containers
- ✅ Dados **são mantidos** entre sessões de desenvolvimento

Para **resetar o banco de dados**:
```bash
docker compose down -v  # Remove os volumes também
docker compose up --build
```

---

## 📝 Variáveis de Ambiente

### Backend (.env ou docker-compose.yml)
```env
DATABASE_URL=postgresql://todo_user:todo_password@db:5432/todo_db
PORT=8000
NODE_ENV=development
CORS_ORIGINS=http://localhost:5173,http://localhost:8080
```

### Frontend
```env
VITE_API_URL=http://localhost:8000/api
```

---

## 🛠️ Desenvolvimento

### Backend (Python)

**Instalar dependências localmente** (opcional):
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Rodar localmente** (sem Docker):
```bash
cd backend
uvicorn src.main:app --reload
```

### Frontend (React)

**Instalar dependências localmente** (opcional):
```bash
cd frontend
npm install
```

**Rodar localmente** (sem Docker):
```bash
cd frontend
npm run dev
```

---

## 🔍 Estrutura de Dados

### Task (Tarefa)
```json
{
  "id": 1,
  "title": "Estudar FastAPI",
  "done": false,
  "created_at": "2026-02-23T10:30:00",
  "updated_at": "2026-02-23T10:30:00"
}
```

---

## 📊 Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| 200 | Sucesso (GET, PUT) |
| 201 | Criado (POST) |
| 204 | Sem conteúdo (DELETE) |
| 400 | Erro de validação |
| 404 | Recurso não encontrado |
| 500 | Erro interno do servidor |

---

## 🎨 Clean Code & Boas Práticas

Este projeto segue princípios de código limpo:

- ✅ **Separação de responsabilidades** (routes, services, models)
- ✅ **Nomenclatura clara** e descritiva
- ✅ **Comentários explicativos** onde necessário
- ✅ **Tratamento de erros** consistente
- ✅ **Validação de dados** com Pydantic
- ✅ **Logs estruturados** no backend
- ✅ **Tipagem estática** (Python type hints)
- ✅ **Componentização** no frontend
- ✅ **Código DRY** (Don't Repeat Yourself)

---

## 🚧 Roadmap (Melhorias Futuras)

- [ ] Autenticação e autorização (JWT)
- [ ] Testes automatizados (pytest, Jest)
- [ ] CI/CD com GitHub Actions
- [ ] Deploy em cloud (AWS, Azure, GCP)
- [ ] Suporte a múltiplos usuários
- [ ] Etiquetas e categorias para tarefas
- [ ] Data de vencimento e lembretes
- [ ] Modo escuro
- [ ] Internacionalização (i18n)

---

## 🐛 Solução de Problemas

### Porta já em uso
```bash
# Verifique processos usando as portas
netstat -ano | findstr :8000
netstat -ano | findstr :5173
netstat -ano | findstr :5432

# Ou mude as portas no docker-compose.yml
```

### Banco de dados não conecta
```bash
# Verifique os logs do container
docker compose logs db

# Recrie os containers
docker compose down
docker compose up --build
```

### Frontend não carrega
```bash
# Verifique se o backend está rodando
curl http://localhost:8000/api/health

# Limpe o cache do navegador
# Ou acesse em modo anônimo
```

### Erro de permissão (Linux/Mac)
```bash
# Adicione permissões de execução
chmod +x backend/src/main.py
```

---

## 📄 Licença

Este é um projeto de portfólio livre para uso educacional e demonstração.

---

## 👨‍💻 Autor

Desenvolvido como projeto de portfólio full-stack demonstrando habilidades em:
- Arquitetura de software
- Backend com Python/FastAPI
- Frontend com React
- DevOps com Docker
- Boas práticas de desenvolvimento

---

## 📚 Recursos Adicionais

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Documentação React](https://react.dev/)
- [Documentação Vite](https://vitejs.dev/)
- [Documentação Docker](https://docs.docker.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)

---

**⭐ Se este projeto foi útil, considere dar uma estrela no repositório!**
