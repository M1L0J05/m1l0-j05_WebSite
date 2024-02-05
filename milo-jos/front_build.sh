#!/bin/bash

source .venv/bin/activate

pip install --upgrade pip

rm -rf public

reflex init
reflex expor --frontend-only
unzip -f frontend.zip -d public
rm -f frontend.zip
deactivate