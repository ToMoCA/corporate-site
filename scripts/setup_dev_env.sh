#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

cd $SCRIPT_DIR/../

git submodule init
git submodule update
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
