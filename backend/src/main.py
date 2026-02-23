"""
Ponto de entrada da aplicação FastAPI.
Configura rotas, middlewares e inicialização do banco.
"""
import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import tasks

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="To-Do API",
    description="API REST para gerenciamento de tarefas",
    version="1.0.0"
)

# Configuração de CORS
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:8080").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware para logging de requisições
@app.middleware("http")
async def log_requests(request, call_next):
    """Middleware para logar todas as requisições."""
    logger.info(f"{request.method} {request.url.path}")
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.error(f"Erro ao processar requisição: {str(e)}")
        raise


# Rota de health check
@app.get("/api/health")
def health_check():
    """
    Endpoint de verificação de saúde da API.
    Retorna status ok se o servidor está rodando.
    """
    return {"status": "ok"}


# Inclui as rotas de tarefas
app.include_router(tasks.router)


# Tratamento global de exceções
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Captura e loga exceções não tratadas."""
    logger.error(f"Erro inesperado: {str(exc)}")
    return {
        "detail": "Erro interno do servidor",
        "status_code": 500
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
