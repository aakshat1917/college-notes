#!/usr/bin/env bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser only if it doesn't exist (optional)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell
