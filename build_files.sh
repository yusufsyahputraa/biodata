#!/bin/bash

set -e

pip install --break-system-packages -r requirements.txt

mkdir -p staticfiles_build/static

python manage.py collectstatic --noinput --clear