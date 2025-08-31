#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Current directory: $(pwd)"
echo "Directory contents:"
ls -la

# Check if we're in the right directory
if [ -f "manage.py" ]; then
    echo "Found manage.py in current directory"
elif [ -d "asset-helpdesk-workflow" ]; then
    echo "Moving to asset-helpdesk-workflow directory"
    cd asset-helpdesk-workflow
    if [ ! -f "manage.py" ]; then
        echo "Error: manage.py not found in asset-helpdesk-workflow"
        exit 1
    fi
else
    echo "Error: Cannot find manage.py or asset-helpdesk-workflow directory"
    exit 1
fi

echo "Installing requirements..."
pip install -r requirements.txt

echo "Running Django commands..."
python manage.py check
python manage.py collectstatic --no-input
python manage.py migrate