#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Build Debug Info ==="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"
echo "Directory contents:"
ls -la

echo "=== Installing Requirements ==="
pip install -r requirements.txt

echo "=== Django Setup ==="
python manage.py check --list
python manage.py collectstatic --no-input
python manage.py migrate