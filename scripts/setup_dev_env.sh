#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

cd $SCRIPT_DIR/../

git submodule init
git submodule update
python3.6 -m venv .env
source .env/bin/activate
pip3.6 install -r requirements.txt
