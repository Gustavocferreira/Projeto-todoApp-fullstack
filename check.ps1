# Script de verificação de ambiente

Write-Host "================================" -ForegroundColor Cyan
Write-Host "   Verificação de Ambiente     " -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Verifica Docker
Write-Host "1. Docker:" -ForegroundColor Yellow
if (Get-Command docker -ErrorAction SilentlyContinue) {
    $dockerVersion = docker --version
    Write-Host "   ✓ $dockerVersion" -ForegroundColor Green
} else {
    Write-Host "   ✗ Docker não encontrado" -ForegroundColor Red
}

# Verifica Docker Compose
Write-Host "2. Docker Compose:" -ForegroundColor Yellow
if (Get-Command docker-compose -ErrorAction SilentlyContinue) {
    $composeVersion = docker-compose --version
    Write-Host "   ✓ $composeVersion" -ForegroundColor Green
} else {
    Write-Host "   ✗ Docker Compose não encontrado" -ForegroundColor Red
}

# Verifica status dos containers
Write-Host "3. Status dos Containers:" -ForegroundColor Yellow
$containers = docker ps --filter "name=todo" --format "{{.Names}} - {{.Status}}"
if ($containers) {
    foreach ($container in $containers) {
        Write-Host "   ✓ $container" -ForegroundColor Green
    }
} else {
    Write-Host "   • Nenhum container em execução" -ForegroundColor Gray
}

# Verifica portas
Write-Host "4. Portas em Uso:" -ForegroundColor Yellow
$ports = @(8000, 5173, 5432)
foreach ($port in $ports) {
    $connection = Test-NetConnection -ComputerName localhost -Port $port -InformationLevel Quiet -WarningAction SilentlyContinue
    if ($connection) {
        Write-Host "   ✓ Porta $port está em uso" -ForegroundColor Green
    } else {
        Write-Host "   • Porta $port está livre" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "URLs da Aplicação:" -ForegroundColor Cyan
Write-Host "  Frontend:  http://localhost:5173" -ForegroundColor White
Write-Host "  Backend:   http://localhost:8000" -ForegroundColor White
Write-Host "  API Docs:  http://localhost:8000/docs" -ForegroundColor White
Write-Host "================================" -ForegroundColor Cyan
