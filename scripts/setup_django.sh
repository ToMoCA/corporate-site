#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

source $SCRIPT_DIR/../.env/bin/activate

cd $SCRIPT_DIR/../project/

./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser

# ./manage.py dumpdata products --format=json --indent=2 > products.json
# ./manage.py loaddata products
cd $SCRIPT_DIR
python inventory_handler.py


cd $SCRIPT_DIR/../project/

./manage.py collectstatic
./manage.py runserver 0.0.0.0:8080

