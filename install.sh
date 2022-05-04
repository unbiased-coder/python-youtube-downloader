#!/bin/bash

echo "Cleaning up old directories"
rm -rf venv pytube
export ROOT_DIR=`pwd`
echo "Setting up virtual environment"
virtualenv venv
. venv/bin/activate
echo "Installing python requirements"
$ROOT_DIR/venv/bin/pip install -r requirements.txt
echo "Cloning Pytube"
git clone https://github.com/pytube/pytube
echo "Patching cipher.py to work with latest youtube"
cp cipher.py ./pytube/pytube/cipher.py
cd pytube
echo "Building Pytube"
$ROOT_DIR/venv/bin/python setup.py build
$ROOT_DIR/venv/bin/python setup.py install
