#!/usr/bin/env bash

# $ crontab -e
# */1 * * * * $HOME/workspace/swm/django/arduino.sh

# $HOME (home of cron user)

source $HOME/.virtualenvs/swm/bin/activate
cd $HOME/workspace/swm/django/
$HOME/.virtualenvs/swm/bin/python $HOME/workspace/swm/django/main/arduino.py
