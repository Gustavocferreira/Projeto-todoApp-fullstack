"""
Modelos SQLAlchemy para o banco de dados.
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base


class Task(Base):
    """
    Modelo de Task (tarefa) no banco de dados.
    
    Campos:
    - id: identificador único
    - title: título da tarefa (3-80 caracteres)
    - done: status de conclusão (padrão: False)
    - created_at: data/hora de criação (auto-gerado)
    - updated_at: data/hora de atualização (auto-atualizado)
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(80), nullable=False)
    done = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
