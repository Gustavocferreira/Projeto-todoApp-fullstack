"""
Rotas da API para gerenciamento de tarefas.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import TaskCreate, TaskUpdate, TaskResponse
from ..services.task_service import TaskService

# Router para endpoints de tarefas
router = APIRouter(prefix="/api/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskResponse])
def get_all_tasks(db: Session = Depends(get_db)):
    """
    Retorna todas as tarefas.
    Ordenadas por data de criação (mais nova primeiro).
    """
    tasks = TaskService.get_all_tasks(db)
    return tasks


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova tarefa.
    
    Validações:
    - Title obrigatório (3-80 caracteres)
    - Title não pode ser vazio ou apenas espaços
    """
    try:
        task = TaskService.create_task(db, task_data)
        return task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro ao criar tarefa: {str(e)}"
        )


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retorna uma tarefa específica por ID.
    """
    task = TaskService.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    """
    Atualiza uma tarefa existente.
    
    Permite atualizar:
    - title: novo título da tarefa
    - done: status de conclusão (true/false)
    """
    task = TaskService.update_task(db, task_id, task_data)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Deleta uma tarefa.
    
    Retorna 204 No Content se bem-sucedido.
    """
    deleted = TaskService.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
