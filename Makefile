COMPOSE_FILE := docker-compose.yml
SERVICE_NAME := api

.PHONY: all up down build rebuild run test clean

all: up

build:
	docker compose -f $(COMPOSE_FILE) build

rebuild:
	docker compose -f $(COMPOSE_FILE) build --no-cache

up:
	docker compose -f $(COMPOSE_FILE) up --build

run:
	docker compose -f $(COMPOSE_FILE) up --build -d

test:
	docker compose -f $(COMPOSE_FILE) run --rm $(SERVICE_NAME) python -m unittest discover tests

down:
	docker compose -f $(COMPOSE_FILE) down

clean: down
	docker system prune -f
