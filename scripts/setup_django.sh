#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

cd $SCRIPT_DIR/../project/

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
# ./manage.py dumpdata products --format=json --indent=2 > products.json
./manage.py loaddata products
./manage.py runserver 0.0.0.0:8080
