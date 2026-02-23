# 🏗️ Arquitetura e Padrões

## Visão Geral

Este projeto implementa uma arquitetura em camadas (layered architecture) com separação clara de responsabilidades.

## Estrutura do Backend (FastAPI)

### Camadas

```
┌─────────────────────────────────┐
│         Rotas (Routes)          │  ← Interface HTTP (endpoints)
├─────────────────────────────────┤
│       Serviços (Services)       │  ← Lógica de negócio
├─────────────────────────────────┤
│       Modelos (Models)          │  ← Camada de dados (ORM)
├─────────────────────────────────┤
│    Banco de Dados (PostgreSQL)  │  ← Persistência
└─────────────────────────────────┘
```

### 1. Rotas (`routes/tasks.py`)

**Responsabilidade**: Lidar com requisições HTTP
- Validação de entrada (via Pydantic schemas)
- Chamada aos serviços
- Tratamento de exceções HTTP
- Serialização de resposta

**Exemplo**:
```python
@router.get("", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = TaskService.get_all_tasks(db)
    return tasks
```

### 2. Serviços (`services/task_service.py`)

**Responsabilidade**: Implementar regras de negócio
- Operações CRUD
- Validações de negócio
- Transformações de dados
- Orquestração de operações complexas

**Exemplo**:
```python
class TaskService:
    @staticmethod
    def create_task(db: Session, task_data: TaskCreate) -> Task:
        new_task = Task(title=task_data.title, done=False)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
```

### 3. Modelos (`models.py`)

**Responsabilidade**: Definir estrutura de dados
- Mapeamento objeto-relacional (ORM)
- Definição de tabelas
- Relacionamentos (se houver)

**Exemplo**:
```python
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(80), nullable=False)
    done = Column(Boolean, default=False)
    # ...
```

### 4. Schemas (`schemas.py`)

**Responsabilidade**: Validação e serialização
- Validação de entrada (request)
- Serialização de saída (response)
- Transformações de tipo

**Exemplo**:
```python
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=80)
    
    @field_validator('title')
    def title_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("O título não pode ser vazio")
        return v.strip()
```

### 5. Database (`database.py`)

**Responsabilidade**: Configuração de conexão
- Engine do SQLAlchemy
- Sessão de banco de dados
- Dependency injection (`get_db`)

---

## Estrutura do Frontend (React)

### Arquitetura de Componentes

```
┌─────────────────────────────────┐
│            App.jsx              │  ← Componente principal
│  ┌──────────────────────────┐   │
│  │   Estado da aplicação    │   │  ← useState, useEffect
│  │   (tasks, loading, etc)  │   │
│  └──────────────────────────┘   │
│  ┌──────────────────────────┐   │
│  │   Lógica de API          │   │  ← fetch, handlers
│  │   (fetchTasks, create)   │   │
│  └──────────────────────────┘   │
│  ┌──────────────────────────┐   │
│  │   Renderização UI        │   │  ← JSX, componentes
│  └──────────────────────────┘   │
└─────────────────────────────────┘
```

### Fluxo de Dados

1. **Usuário interage** → Evento (onClick, onChange)
2. **Handler processa** → Chama API
3. **API responde** → Atualiza estado
4. **Estado muda** → React re-renderiza
5. **UI atualizada** → Usuário vê resultado

---

## Padrões Implementados

### 1. Repository Pattern (implícito)
Os serviços atuam como repositórios, abstraindo o acesso aos dados.

### 2. Dependency Injection
```python
def get_all_tasks(db: Session = Depends(get_db)):
    # 'db' é injetado automaticamente pelo FastAPI
```

### 3. Data Transfer Objects (DTOs)
Schemas Pydantic servem como DTOs para transferência de dados entre camadas.

### 4. Single Responsibility Principle
- Rotas: apenas endpoints HTTP
- Serviços: apenas lógica de negócio
- Modelos: apenas definição de dados

### 5. Clean Architecture Principles
- Dependências apontam para dentro
- Camadas externas dependem de camadas internas
- Lógica de negócio isolada de frameworks

---

## Fluxo de uma Requisição

### Exemplo: Criar uma nova tarefa

```
1. Frontend (App.jsx)
   └─ handleCreateTask() é chamado
      └─ fetch POST /api/tasks com { title: "..." }

2. Backend (FastAPI)
   └─ Rota tasks.py recebe a requisição
      └─ Valida dados com TaskCreate (Pydantic)
         └─ Chama TaskService.create_task()
            └─ Cria objeto Task (SQLAlchemy)
               └─ Salva no PostgreSQL
                  └─ Retorna Task criada
                     └─ Serializa com TaskResponse
                        └─ Retorna JSON para frontend

3. Frontend (App.jsx)
   └─ Recebe resposta
      └─ Atualiza estado (chamando fetchTasks)
         └─ React re-renderiza a lista
```

---

## Tratamento de Erros

### Backend
```python
try:
    # Operação
except Exception as e:
    logger.error(f"Erro: {str(e)}")
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Erro interno"
    )
```

### Frontend
```javascript
try {
    const response = await fetch(...)
    if (!response.ok) {
        throw new Error('Erro ao carregar')
    }
    // Sucesso
} catch (err) {
    setError(err.message)
    console.error('Erro:', err)
}
```

---

## Segurança

### CORS
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,  # Define origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Validação
- Entrada validada com Pydantic
- Tipos verificados em tempo de execução
- SQL Injection prevenido pelo SQLAlchemy

---

## Performance

### Backend
- **Async/Await**: FastAPI suporta operações assíncronas
- **Connection Pooling**: SQLAlchemy gerencia pool de conexões
- **Índices**: Campo `id` indexado no banco

### Frontend
- **Vite**: Build ultra-rápida
- **React 18**: Rendering otimizado
- **Lazy Loading**: Pode ser implementado para grandes listas

---

## Escalabilidade

### Horizontal
- Backend stateless permite múltiplas instâncias
- Load balancer pode distribuir tráfego
- Banco pode ser replicado (read replicas)

### Vertical
- Aumentar recursos do container
- Otimizar queries do banco
- Implementar cache (Redis)

---

## Observabilidade

### Logs
```python
logger.info(f"{request.method} {request.url.path}")
```

### Health Check
```http
GET /api/health
→ {"status": "ok"}
```

### Metrics (futuro)
- Prometheus para métricas
- Grafana para visualização
- Tempo de resposta, taxa de erro, etc.

---

## Testes (futuro)

### Backend
```python
# pytest
def test_create_task():
    response = client.post("/api/tasks", json={"title": "Test"})
    assert response.status_code == 201
```

### Frontend
```javascript
// Jest + React Testing Library
test('renders todo app', () => {
    render(<App />)
    expect(screen.getByText(/To-Do App/i)).toBeInTheDocument()
})
```

---

## Convenções de Código

### Python
- PEP 8 (style guide)
- Type hints em funções
- Docstrings em classes e funções

### JavaScript/React
- camelCase para variáveis
- PascalCase para componentes
- Arrow functions para componentes

### Git
- Commits semânticos: `feat:`, `fix:`, `docs:`, etc.
- Branches: `feature/`, `bugfix/`, `hotfix/`

---

## Referências

- [FastAPI Best Practices](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [React Design Patterns](https://react.dev/learn/thinking-in-react)
- [Clean Architecture (Uncle Bob)](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
