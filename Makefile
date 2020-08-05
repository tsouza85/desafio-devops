PYTHON = python3

install:
	pip install -r requirements.txt

lint:
	flake8 **/*.py
	pylint --exit-zero **/*.py

test:
	pytest

run:
	${PYTHON} src/app.py
