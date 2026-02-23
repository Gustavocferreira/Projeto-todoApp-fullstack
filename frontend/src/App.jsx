import { useState, useEffect } from 'react'
import './App.css'

// URL base da API
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

function App() {
  // Estados da aplicação
  const [tasks, setTasks] = useState([])
  const [newTaskTitle, setNewTaskTitle] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  /**
   * Carrega todas as tarefas da API ao iniciar
   */
  useEffect(() => {
    fetchTasks()
  }, [])

  /**
   * Busca todas as tarefas do backend
   */
  const fetchTasks = async () => {
    try {
      setLoading(true)
      setError(null)
      const response = await fetch(`${API_BASE_URL}/tasks`)
      
      if (!response.ok) {
        throw new Error('Erro ao carregar tarefas')
      }
      
      const data = await response.json()
      setTasks(data)
    } catch (err) {
      setError(err.message)
      console.error('Erro ao buscar tarefas:', err)
    } finally {
      setLoading(false)
    }
  }

  /**
   * Cria uma nova tarefa
   */
  const handleCreateTask = async (e) => {
    e.preventDefault()
    
    // Validação básica
    if (!newTaskTitle.trim()) {
      setError('O título não pode ser vazio')
      return
    }

    if (newTaskTitle.trim().length < 3 || newTaskTitle.trim().length > 80) {
      setError('O título deve ter entre 3 e 80 caracteres')
      return
    }

    try {
      setLoading(true)
      setError(null)
      
      const response = await fetch(`${API_BASE_URL}/tasks`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title: newTaskTitle.trim() }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Erro ao criar tarefa')
      }

      // Limpa o input e recarrega a lista
      setNewTaskTitle('')
      await fetchTasks()
    } catch (err) {
      setError(err.message)
      console.error('Erro ao criar tarefa:', err)
    } finally {
      setLoading(false)
    }
  }

  /**
   * Alterna o status de conclusão de uma tarefa
   */
  const handleToggleDone = async (taskId, currentDone) => {
    try {
      setError(null)
      
      const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ done: !currentDone }),
      })

      if (!response.ok) {
        throw new Error('Erro ao atualizar tarefa')
      }

      // Atualiza a lista
      await fetchTasks()
    } catch (err) {
      setError(err.message)
      console.error('Erro ao atualizar tarefa:', err)
    }
  }

  /**
   * Deleta uma tarefa
   */
  const handleDeleteTask = async (taskId) => {
    if (!window.confirm('Deseja realmente excluir esta tarefa?')) {
      return
    }

    try {
      setError(null)
      
      const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
        method: 'DELETE',
      })

      if (!response.ok) {
        throw new Error('Erro ao excluir tarefa')
      }

      // Atualiza a lista
      await fetchTasks()
    } catch (err) {
      setError(err.message)
      console.error('Erro ao excluir tarefa:', err)
    }
  }

  /**
   * Formata data para exibição
   */
  const formatDate = (dateString) => {
    const date = new Date(dateString)
    return date.toLocaleDateString('pt-BR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    })
  }

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1>📝 To-Do App</h1>
          <p>Gerencie suas tarefas de forma simples e eficiente</p>
        </header>

        {/* Formulário de criação */}
        <form onSubmit={handleCreateTask} className="task-form">
          <input
            type="text"
            placeholder="Digite uma nova tarefa..."
            value={newTaskTitle}
            onChange={(e) => setNewTaskTitle(e.target.value)}
            disabled={loading}
            maxLength={80}
            className="task-input"
          />
          <button type="submit" disabled={loading} className="btn-primary">
            {loading ? 'Adicionando...' : 'Adicionar'}
          </button>
        </form>

        {/* Exibição de erros */}
        {error && (
          <div className="error-message">
            ⚠️ {error}
            <button onClick={() => setError(null)} className="btn-close">×</button>
          </div>
        )}

        {/* Lista de tarefas */}
        <div className="tasks-container">
          {loading && tasks.length === 0 ? (
            <div className="loading">Carregando tarefas...</div>
          ) : tasks.length === 0 ? (
            <div className="empty-state">
              <p>Nenhuma tarefa cadastrada</p>
              <p className="empty-subtitle">Adicione uma tarefa acima para começar</p>
            </div>
          ) : (
            <ul className="task-list">
              {tasks.map((task) => (
                <li key={task.id} className={`task-item ${task.done ? 'done' : ''}`}>
                  <div className="task-content">
                    <input
                      type="checkbox"
                      checked={task.done}
                      onChange={() => handleToggleDone(task.id, task.done)}
                      className="task-checkbox"
                    />
                    <div className="task-info">
                      <span className="task-title">{task.title}</span>
                      <span className="task-date">
                        Criada em: {formatDate(task.created_at)}
                      </span>
                    </div>
                  </div>
                  <button
                    onClick={() => handleDeleteTask(task.id)}
                    className="btn-delete"
                    title="Excluir tarefa"
                  >
                    🗑️
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>

        {/* Estatísticas */}
        {tasks.length > 0 && (
          <div className="stats">
            <span>Total: {tasks.length}</span>
            <span>Concluídas: {tasks.filter(t => t.done).length}</span>
            <span>Pendentes: {tasks.filter(t => !t.done).length}</span>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
