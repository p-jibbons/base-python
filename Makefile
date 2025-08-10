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
	& "venv/Scripts/python.exe" -m unittest discover tests -v

# Run examples
example:
	& "venv/Scripts/python.exe" examples/basic_usage.py

# Clean up cache files
clean:
	Get-ChildItem -Recurse -Name "*.pyc" | Remove-Item -Force
	Get-ChildItem -Recurse -Name "__pycache__" | Remove-Item -Recurse -Force
	Get-ChildItem -Recurse -Name "*.egg-info" | Remove-Item -Recurse -Force

# Code linting (optional - requires flake8)
lint:
	& "venv/Scripts/flake8.exe" src/ tests/ examples/

# Code formatting (optional - requires black)
format:
	& "venv/Scripts/black.exe" src/ tests/ examples/

# Install package
install:
	& "venv/Scripts/pip.exe" install .

# Install in development mode
dev-install:
	& "venv/Scripts/pip.exe" install -e .
	& "venv/Scripts/pip.exe" install -r requirements.txt
