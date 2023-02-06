#!/usr/bin/bash

export PROJECT_FOLDER="workflow_orchestration"

echo "Install pipenv"
sleep 2
pip install pipenv

echo "Create the virtual environment"
sleep 2
cd ~/${PROJECT_FOLDER}
pipenv install --python 3.9 --requirements ./containers/requirements.txt