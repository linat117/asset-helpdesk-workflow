#!/usr/bin/env bash
# exit on error
set -o errexit

echo "=== Build Debug Info ==="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"

echo "=== Installing Packages Individually ==="
pip install setuptools wheel
pip install Django==5.2.5
pip install djangorestframework==3.16.1
pip install PyJWT==2.10.1
pip install djangorestframework-simplejwt==5.3.0
pip install gunicorn==21.2.0
pip install whitenoise==6.6.0
pip install dj-database-url==2.1.0
pip install psycopg2-binary==2.9.9
pip install python-decouple==3.8

echo "=== Checking Django Installation ==="
python -c "import django; print(f'Django version: {django.get_version()}')"
python -c "import whitenoise; print('Whitenoise installed successfully')"
python -c "import rest_framework_simplejwt; print('SimpleJWT installed successfully')"

echo "=== Django Setup ==="
# Force the settings module directly
export DJANGO_SETTINGS_MODULE=asset_helpdesk_workflow.settings_production

echo "Django settings module: $DJANGO_SETTINGS_MODULE"

# Run Django commands with explicit settings
python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asset_helpdesk_workflow.settings_production')
django.setup()
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'check'])
"

python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asset_helpdesk_workflow.settings_production')
django.setup()
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'collectstatic', '--no-input'])
"

python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asset_helpdesk_workflow.settings_production')
django.setup()
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'migrate'])
"