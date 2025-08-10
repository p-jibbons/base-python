# Python Functions Reference - Makefile
# Common commands for development and testing

.PHONY: help test clean lint format install dev-install example

# Default target
help:
	@echo "Available commands:"
	@echo "  test        - Run all tests"
	@echo "  example     - Run usage examples"
	@echo "  clean       - Remove cache files"
	@echo "  lint        - Run code linting (requires flake8)"
	@echo "  format      - Format code (requires black)"
	@echo "  install     - Install package"
	@echo "  dev-install - Install package in development mode"

# Run tests
test:
	python -m unittest discover tests -v

# Run examples
example:
	python examples/basic_usage.py

# Clean up cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

# Code linting (optional - requires flake8)
lint:
	flake8 src/ tests/ examples/

# Code formatting (optional - requires black)
format:
	black src/ tests/ examples/

# Install package
install:
	pip install .

# Install in development mode
dev-install:
	pip install -e .
	pip install -r requirements.txt
