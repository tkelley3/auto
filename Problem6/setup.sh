#!/usr/bin/env bash
apt-get update

# if you need matplotlib, other package?, install that too
apt-get install -y python3 python3-pip python3-dev python3-matplotlib
apt-get install -y python3 python3-pip python3-dev python3-numpy
apt-get install -y python3 python3-pip python3-dev python3-pandas
apt-get install -y python3 python3-pip python3-dev python3-random
apt-get install -y python3 python3-pip python3-dev python3-numpy.random

# requirements.txt will carry some more packages
pip3 install -r /autograder/source/requirements.txt

# printing out the python version to help debug
python3 --version
