.ONESHELL:
SHELL:=/bin/bash

# python version  3.9.17
PYTHON:= "python"

install-requirements:
	pip install -r requirements.txt

data-processing-api-setup-vitualenv:
	@$(PYTHON) -m venv .virtualenvs/data-processing-api
	@. .virtualenvs/data-processing-api/bin/activate
	@pip install --upgrade pip
	@pip install -r requirements.txt

run-data-processing-api:
	@. .virtualenvs/data-processing-api/bin/activate
	@uvicorn src.main:app --reload