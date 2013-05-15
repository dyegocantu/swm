#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time

class Arduino(object):
    
    def connect(self, port, baud_rate):
        self.arduino = serial.Serial(port, baud_rate)
        time.sleep(2)

    def write(self, data):
        self.arduino.write(data)

    def read(self):
        return self.arduino.readline()


if __name__ == '__main__':

    import os
    import json
    import datetime

    if os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swm.settings"):
        from sensor.models import ReadData
        from django.utils import timezone
    else:
        raise

    SERIAL_PORT = '/dev/ttyACM0'
    BAUD_RATE = 115200

    arduino = Arduino()
    arduino.connect(SERIAL_PORT, BAUD_RATE)
    
    arduino.write('1')
    receive = json.loads(arduino.read())
    
    read_data = ReadData()
    read_data.temperature = receive['temperature']
    read_data.humidity = receive['humidity']
    #read_data.created = datetime.datetime.now()
    read_data.created = timezone.now()
    read_data.save()

