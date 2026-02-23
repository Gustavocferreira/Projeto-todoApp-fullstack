# 🚀 Guia Rápido de Início

## Primeira Execução

### Passo 1: Pré-requisitos
✅ Docker Desktop instalado e rodando
✅ Git instalado (se for clonar o repositório)

### Passo 2: Executar
```powershell
# Abra o PowerShell no diretório do projeto e execute:
.\start.ps1
```

**OU usando Docker Compose diretamente:**
```powershell
docker compose up --build
```

### Passo 3: Aguarde
⏳ Primeira execução demora ~3-5 minutos (baixa imagens, instala dependências)

### Passo 4: Acesse
- 🌐 Frontend: http://localhost:5173
- 🔌 Backend API: http://localhost:8000
- 📚 Documentação: http://localhost:8000/docs

---

## Comandos Úteis

### Verificar ambiente
```powershell
.\check.ps1
```

### Parar containers
```powershell
# Ctrl+C no terminal onde está rodando
# OU
docker compose down
```

### Ver logs
```powershell
docker compose logs -f
```

### Resetar banco de dados
```powershell
docker compose down -v
docker compose up --build
```

### Reconstruir tudo do zero
```powershell
docker compose down -v --rmi all
docker compose up --build
```

---

## Verificação Rápida

### Backend está rodando?
```powershell
curl http://localhost:8000/api/health
# Deve retornar: {"status":"ok"}
```

### Containers estão rodando?
```powershell
docker ps
# Deve mostrar: todo-backend, todo-frontend, todo-db
```

---

## Solução Rápida de Problemas

### Porta já em uso
```powershell
# Descubra qual processo está usando a porta
netstat -ano | findstr :8000

# Mate o processo (substitua PID pelo número encontrado)
taskkill /PID <PID> /F
```

### Container não inicia
```powershell
# Veja os logs
docker compose logs backend
docker compose logs frontend
docker compose logs db

# Reconstrua
docker compose down
docker compose build --no-cache
docker compose up
```

### Mudanças não aparecem
```powershell
# Força reconstrução
docker compose up --build --force-recreate
```

---

## Desenvolvimento

### Editar código
1. Edite os arquivos normalmente no VS Code
2. As mudanças são refletidas automaticamente (hot reload)
3. Backend: salvou → recarregou ✅
4. Frontend: salvou → recompilou ✅

### Estrutura básica
```
backend/src/
  ├── main.py           # Ponto de entrada
  ├── routes/tasks.py   # Endpoints da API
  └── services/         # Lógica de negócio

frontend/src/
  ├── App.jsx           # Componente principal
  └── App.css           # Estilos
```

---

## URLs Importantes

| Serviço | URL | Descrição |
|---------|-----|-----------|
| Frontend | http://localhost:5173 | Interface do usuário |
| Backend | http://localhost:8000 | API REST |
| Swagger | http://localhost:8000/docs | Documentação interativa |
| ReDoc | http://localhost:8000/redoc | Documentação alternativa |

---

## Próximos Passos

1. ✅ Testou localmente? Excelente!
2. 📖 Leia o [README.md](README.md) completo
3. 🏗️ Veja [ARCHITECTURE.md](ARCHITECTURE.md) para entender a estrutura
4. 🔧 Personalize conforme suas necessidades
5. 🚀 Faça deploy (quando estiver pronto)

---

## Parar e Limpar

### Parar sem perder dados
```powershell
docker compose down
```

### Parar e limpar TUDO (cuidado!)
```powershell
docker compose down -v --rmi all --remove-orphans
```

---

**💡 Dica**: Use `.\check.ps1` sempre que tiver dúvidas sobre o estado do ambiente!
