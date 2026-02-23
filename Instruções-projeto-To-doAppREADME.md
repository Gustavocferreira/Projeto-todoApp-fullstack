# To-do App (Full-stack simples com Docker)

## 1) Objetivo
Criar uma aplicação de tarefas (To-do) com:
- Backend em Node.js + Express com API REST.
- Frontend simples (HTML/CSS/JS) consumindo a API.
- Execução via Docker (docker compose) em ambiente local.

O foco é portfólio: código limpo, README bom, e funcionamento previsível.

---

## 2) Stack (mínimo)
- Node.js 18+ (backend)
- Express (API)
- Persistência: PostgreSQL (arquivo local) OU JSON file (somente dev)
- Frontend: HTML + CSS + JavaScript (sem framework)
- Docker + Docker Compose

---

## 3) Requisitos funcionais (MVP)

### 3.1 Entidade Task
Campos:
- id: string ou number (gerado pelo sistema)
- title: string (obrigatório, 3 a 80 chars)
- done: boolean (padrão false)
- createdAt: datetime (gerado)
- updatedAt: datetime (gerado)

### 3.2 Regras
- Não permitir title vazio.
- Não permitir title duplicado (opcional; se implementar, documentar).
- Ordenar listagem por createdAt desc (mais nova primeiro).

### 3.3 Endpoints (API REST)
Base URL: `/api`

- GET `/api/health`
  - Retorna `{ status: "ok" }`

- GET `/api/tasks`
  - Retorna lista de tasks

- POST `/api/tasks`
  - Body: `{ "title": "..." }`
  - Cria task e retorna task criada

- PUT `/api/tasks/:id`
  - Body: `{ "title": "..." }` (opcional) e/ou `{ "done": true/false }`
  - Atualiza a task e retorna task atualizada

- DELETE `/api/tasks/:id`
  - Remove a task e retorna 204 (sem body)

### 3.4 Códigos e erros
- 400 para validação (ex.: title inválido)
- 404 se task não existir
- 500 para erros inesperados (com log no servidor)

---

## 4) Requisitos não-funcionais (mínimo)
- CORS habilitado para o frontend local.
- Logs básicos no backend (request + error).
- Variáveis de ambiente para porta e modo:
  - `PORT` (padrão 3000)
  - `NODE_ENV` (development/production)

---

## 5) Frontend (mínimo)
Uma página com:
- Input + botão "Adicionar"
- Lista de tarefas
- Checkbox para marcar como concluída
- Botão para excluir

Integração:
- O frontend deve chamar a API do backend (fetch).
- Ao iniciar, carregar a lista com GET `/api/tasks`.

---

## 6) Docker (mínimo)
### 6.1 Serviços
- `backend`: Node + Express
- `frontend`: pode ser opcional (escolher uma das opções abaixo)

Opção A (mais simples): backend também serve arquivos estáticos do frontend.
- Backend serve `/` com os arquivos do frontend.

Opção B (2 containers): frontend servido por Nginx.
- Frontend em `http://localhost:8080`
- Backend em `http://localhost:3000`

### 6.2 Compose
Requisitos:
- `docker compose up --build` deve subir tudo.
- Portas expostas:
  - backend: 3000:3000
  - (se existir) frontend: 8080:80

Persistência (se usar SQLite):
- O arquivo do banco deve ficar em volume para não perder dados ao recriar container.

---

## 7) Estrutura de pastas (sugestão)
- `/backend`
  - `/src`
    - `index.js` (bootstrap do servidor)
    - `/routes` (rotas)
    - `/services` (regras/uso)
    - `/db` (acesso a dados)
- `/frontend`
  - `index.html`
  - `style.css`
  - `script.js`
- `docker-compose.yml`
- `README.md`

---

## 8) Critérios de aceitação
- `docker compose up --build` sobe sem erros.
- Acessando a UI, consigo:
  - Criar tarefas
  - Listar tarefas
  - Marcar/desmarcar como done
  - Excluir tarefas
- Se eu reiniciar os containers, os dados permanecem (se persistência estiver implementada).
- README explica como rodar.

---

## 9) Fora de escopo (não fazer no MVP)
- Login/autenticação
- Deploy em cloud
- Testes automatizados completos (pode ser bônus)
- UI avançada / Design system
