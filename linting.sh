#!/bin/bash

# Run isort
poetry run isort .

# Run black
poetry run black .

# Run mypy
poetry run mypy .