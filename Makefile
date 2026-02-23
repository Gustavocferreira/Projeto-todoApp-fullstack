# Makefile para facilitar comandos comuns

.PHONY: help up down restart logs clean build test

help:
	@echo "Comandos disponíveis:"
	@echo "  make up        - Inicia todos os containers"
	@echo "  make down      - Para todos os containers"
	@echo "  make restart   - Reinicia todos os containers"
	@echo "  make logs      - Mostra logs de todos os containers"
	@echo "  make clean     - Remove containers, volumes e imagens"
	@echo "  make build     - Reconstrói as imagens"
	@echo "  make db-reset  - Reseta o banco de dados"

up:
	docker compose up --build

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f

clean:
	docker compose down -v --rmi all

build:
	docker compose build --no-cache

db-reset:
	docker compose down -v
	docker compose up --build
