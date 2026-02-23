"""
Serviços de negócio para operações com tarefas.
"""
from sqlalchemy.orm import Session
from ..models import Task
from ..schemas import TaskCreate, TaskUpdate


class TaskService:
    """Serviço responsável pelas regras de negócio de tarefas."""

    @staticmethod
    def get_all_tasks(db: Session) -> list[Task]:
        """
        Retorna todas as tarefas ordenadas por data de criação (mais nova primeiro).
        
        Args:
            db: Sessão do banco de dados
            
        Returns:
            Lista de tarefas
        """
        return db.query(Task).order_by(Task.created_at.desc()).all()

    @staticmethod
    def get_task_by_id(db: Session, task_id: int) -> Task | None:
        """
        Busca uma tarefa por ID.
        
        Args:
            db: Sessão do banco de dados
            task_id: ID da tarefa
            
        Returns:
            Tarefa encontrada ou None
        """
        return db.query(Task).filter(Task.id == task_id).first()

    @staticmethod
    def create_task(db: Session, task_data: TaskCreate) -> Task:
        """
        Cria uma nova tarefa.
        
        Args:
            db: Sessão do banco de dados
            task_data: Dados para criação da tarefa
            
        Returns:
            Tarefa criada
        """
        new_task = Task(title=task_data.title, done=False)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task

    @staticmethod
    def update_task(db: Session, task_id: int, task_data: TaskUpdate) -> Task | None:
        """
        Atualiza uma tarefa existente.
        
        Args:
            db: Sessão do banco de dados
            task_id: ID da tarefa
            task_data: Dados para atualização
            
        Returns:
            Tarefa atualizada ou None se não encontrada
        """
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        
        # Atualiza apenas os campos fornecidos
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.done is not None:
            task.done = task_data.done
        
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def delete_task(db: Session, task_id: int) -> bool:
        """
        Deleta uma tarefa.
        
        Args:
            db: Sessão do banco de dados
            task_id: ID da tarefa
            
        Returns:
            True se deletada, False se não encontrada
        """
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return False
        
        db.delete(task)
        db.commit()
        return True
