install:
	uv sync

build:
	./build.sh

lint:
	uv run ruff check .

render-start:
	uv run gunicorn task_manager.wsgi

django-tests:
	uv run manage.py test

test-coverage:
	uv run coverage run --source=task_manager,users,statuses,labels,tasks manage.py test
	uv run coverage xml
