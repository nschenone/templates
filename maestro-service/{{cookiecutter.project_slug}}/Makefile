.DEFAULT_GOAL := help

SRC ?= src

#################################################################################
# COMMANDS                                                                      #
#################################################################################

.PHONY: help
help: ## Display available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all:
	$(error please pick a target)

up: ## Start Docker application
	docker compose up -d --build

down: ## Stop Docker application
	docker compose down

restart: down up ## Restart Docker application

.PHONY: clean
clean: ## Delete all compiled Python files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist

.PHONY: fmt
fmt: clean ## Format the code (using black and isort)
	@echo "Running black fmt..."
	black $(SRC) .
	isort $(SRC) .

.PHONY: fmt-check
fmt-check: clean ## Format and check the code (using black and isort)
	@echo "Running black+isort fmt check..."
	black --check --diff $(SRC) .
	isort --check --diff $(SRC) .
