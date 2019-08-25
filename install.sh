#!/bin/bash
apt install python-tk
apt install vim
{ crontab -l -u root; echo '* * * * * /opt/mini-gauge/bluetooth_search.sh'; } | crontab -u root -
apt-get install --no-install-recommends bluetooth htop python-dev python-pip -y
service bluetooth start
service bluetooth status
hcitool scan
pip install obd psutil netifaces

