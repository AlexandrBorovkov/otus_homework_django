install:
	uv sync

makemigrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

start:
	uv run manage.py runserver

lint:
	uv run ruff check

test:
	uv run manage.py test