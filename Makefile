.PHONY: install test lint

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

format:
	black app.py
