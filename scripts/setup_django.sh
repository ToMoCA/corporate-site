#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

cd $SCRIPT_DIR/../project/

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8080
