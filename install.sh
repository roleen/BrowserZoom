#!/bin/bash
set -e

unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
	#apt-get update
	apt-get install -y python-pip
	apt-get install xvfb
fi

pip install -r requirements.txt
echo ""
