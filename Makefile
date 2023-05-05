SHELL=/bin/bash
APP=domain

env: ## make virtual environment
env: 
	@echo "Creating virtual environment..."
	@python3 -m venv .venv 

config: ## config git username and e-mail.
config:
	git config --global user.email "gomes.luiz@gmail.com"
	git config --global user.name "Luiz Gomes"

deps: ## install required packages.
deps: 
	@echo "Installing package dependencies..."
	@python3 -m pip install --upgrade pip
	@pip install black coverage flake8 mypy pylint pytest tox
	@pip install -r requirements.txt

freeze: ## update requirements.txt file.
freeze:
	@echo "Freezing package dependencies..."
	pip freeze > requirements.txt

lint: # Lint flask application in debug mode.
lint: 
	@flake8 $(APP)

test: # Test flask application.
test: 
	@pytest -ra tests/

cov: # Print coverage report
cov: 
	@coverage report

push: # Push application for gihub repository.
push:
	@git push && git push --tags

log: # Display git log
log:
	@git log --oneline --decorate --graph --all

amend: # Ammend the commit
amend: 
	@git commit --amend

reset: # Reset to the HEAD
reset:
	@git branch backup
	@git reset --hard HEAD~1

commit:
commit:
	@git add . && git commit 