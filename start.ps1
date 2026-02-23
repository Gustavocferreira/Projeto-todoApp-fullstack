# Script PowerShell para inicialização rápida do projeto

Write-Host "================================" -ForegroundColor Cyan
Write-Host "   To-Do App - Inicializando   " -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se Docker está instalado
Write-Host "Verificando Docker..." -ForegroundColor Yellow
if (Get-Command docker -ErrorAction SilentlyContinue) {
    Write-Host "✓ Docker encontrado" -ForegroundColor Green
} else {
    Write-Host "✗ Docker não encontrado. Por favor, instale o Docker Desktop." -ForegroundColor Red
    exit 1
}

# Verifica se Docker Compose está disponível
Write-Host "Verificando Docker Compose..." -ForegroundColor Yellow
if (Get-Command docker-compose -ErrorAction SilentlyContinue) {
    Write-Host "✓ Docker Compose encontrado" -ForegroundColor Green
} else {
    Write-Host "✗ Docker Compose não encontrado. Por favor, instale o Docker Compose." -ForegroundColor Red
    exit 1
}

# Para containers existentes (se houver)
Write-Host ""
Write-Host "Parando containers existentes (se houver)..." -ForegroundColor Yellow
docker compose down 2>$null

# Constrói e inicia os containers
Write-Host ""
Write-Host "Construindo e iniciando containers..." -ForegroundColor Yellow
Write-Host "Isso pode levar alguns minutos na primeira execução..." -ForegroundColor Gray
Write-Host ""

docker compose up --build

# Nota: O comando acima é bloqueante, então as mensagens abaixo só aparecem após Ctrl+C
Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "   Containers parados          " -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
