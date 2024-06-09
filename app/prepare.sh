#!/bin/sh

python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --no-input
mv frontend/cctv.png static/cctv.png
mv frontend/lamp.png static/lamp.png
mv frontend/sidewalk.png static/sidewalk.png
echo "Preparation done!"
