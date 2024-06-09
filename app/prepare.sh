#!/bin/sh

python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --no-input
mv frontend/cctv.png static/cctv.png
mv frontend/light.jpg static/light.jpg
mv frontend/sideWalk.png static/sideWalk.png
echo "Preparation done!"
