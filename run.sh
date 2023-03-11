#!/usr/bin/env bash

virtual_environment="venv"
requirements="requirements.txt"

if [ ! -d "${virtual_environment}" ]; then
  python3 -m venv ${virtual_environment}
fi

if [ ! -f "${requirements}" ]; then
  echo "Could not find the ${requirements} file."
  exit
fi

source ${virtual_environment}/bin/activate
pip3 install -r ${requirements}
python3 main.py
