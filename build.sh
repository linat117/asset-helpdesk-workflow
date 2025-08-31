#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Build Debug Info ==="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"

echo "=== Installing Requirements ==="
pip install -r requirements.txt

echo "=== Checking Django Installation ==="
python -c "import django; print(f'Django version: {django.get_version()}')"
python -c "import whitenoise; print('Whitenoise installed successfully')"

echo "=== Django Setup ==="
python manage.py check
python manage.py collectstatic --no-input
python manage.py migrate