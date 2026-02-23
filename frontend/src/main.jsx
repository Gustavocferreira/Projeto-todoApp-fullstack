import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

/**
 * Ponto de entrada da aplicação React.
 * Renderiza o componente App no elemento root do HTML.
 */
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
