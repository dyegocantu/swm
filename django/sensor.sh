#!/usr/bin/env bash

# $ crontab -e
# */1 * * * * /home/dyego/workspace/swm/django/sensor.sh

source /home/dyego/.virtualenvs/swm/bin/activate
cd /home/dyego/workspace/swm/django/
/home/dyego/.virtualenvs/swm/bin/python /home/dyego/workspace/swm/django/arduino_interface.py
