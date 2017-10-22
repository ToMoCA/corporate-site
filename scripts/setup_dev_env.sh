#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

cd $SCRIPT_DIR/../

git submodule init
git submodule update
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
