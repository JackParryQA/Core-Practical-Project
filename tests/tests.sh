#!/bin/bash

# Install requirements/create venv
sudo apt-get update
sudo apt-get install python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r test_requirements.txt

# pytest coverage service-1
cd service-1
python3 -m pytest --cov=application
cd ..

# pytest coverage service-2
cd service-2
python3 -m pytest --cov=application
cd ..

# pytest coverage service-3
cd service-3
python3 -m pytest --cov=application
cd ..

# pytest coverage service-4
cd service-4
python3 -m pytest --cov=application
cd ..
