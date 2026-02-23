"""
Configuração do banco de dados e sessão SQLAlchemy.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco (variável de ambiente)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://todo_user:todo_password@db:5432/todo_db")

# Engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()


def get_db():
    """
    Dependency para obter uma sessão de banco de dados.
    Garante que a sessão seja fechada após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
