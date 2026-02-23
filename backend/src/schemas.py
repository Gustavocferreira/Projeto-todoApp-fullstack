"""
Schemas Pydantic para validação e serialização de dados.
"""
from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class TaskCreate(BaseModel):
    """Schema para criação de uma nova tarefa."""
    title: str = Field(..., min_length=3, max_length=80, description="Título da tarefa")

    @field_validator('title')
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        """Valida que o título não seja apenas espaços em branco."""
        if not v or not v.strip():
            raise ValueError("O título não pode ser vazio")
        return v.strip()


class TaskUpdate(BaseModel):
    """Schema para atualização de uma tarefa existente."""
    title: str | None = Field(None, min_length=3, max_length=80, description="Título da tarefa")
    done: bool | None = Field(None, description="Status de conclusão")

    @field_validator('title')
    @classmethod
    def title_not_empty(cls, v: str | None) -> str | None:
        """Valida que o título não seja apenas espaços em branco."""
        if v is not None and (not v or not v.strip()):
            raise ValueError("O título não pode ser vazio")
        return v.strip() if v else None


class TaskResponse(BaseModel):
    """Schema de resposta para uma tarefa."""
    id: int
    title: str
    done: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Permite conversão de objetos SQLAlchemy
