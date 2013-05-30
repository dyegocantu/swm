#!/usr/bin/env bash

# $ crontab -e
# */1 * * * * $HOME/workspace/swm/django/sensor.sh

# $HOME (home of crontab user)

source $HOME/.virtualenvs/swm/bin/activate
cd $HOME/workspace/swm/django/
$HOME/.virtualenvs/swm/bin/python $HOME/workspace/swm/django/arduino_interface.py
