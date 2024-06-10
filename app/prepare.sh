#!/bin/sh

python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --no-input
mv frontend/*.png static/
echo "Preparation done!"
