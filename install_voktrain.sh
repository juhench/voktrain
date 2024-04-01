#!/bin/bash

# installation script for voktrain

sudo apt -y update
sudo apt -y upgrade
sudo apt install -y python3 python3-pip python3-venv build-essential
python3 -m venv voktrain-venv
source ./voktrain-venv/bin/activate
pip install pandas
pip install openpyxl
pip install IPython
mkdir -p ~/Vokabeldateien
echo "Installation of vocabulary trainer completed."
