install:
	uv sync

makemigrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

start:
	uv run python manage.py runserver