#!/bin/sh
set -e

echo "Running tests .."
pytest --cov-report term --cov=app tests/
