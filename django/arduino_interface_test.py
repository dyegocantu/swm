#!/usr/bin/env python
# -*- coding: utf-8 -*-

from serial import Serial
from time import sleep

class Arduino(object):
    
    def connect(self, port, baud_rate):
        self.arduino = Serial(port, baud_rate)
        sleep(2)

    def write(self, data):
        self.arduino.write(data)

    def read(self):
        return self.arduino.readline()


if __name__ == '__main__':

    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swm.settings")

    from arduino_interface.models import ReadData

    SERIAL_PORT = '/dev/ttyACM0'
    BAUD_RATE = 115200

    arduino = Arduino()
    arduino.connect(SERIAL_PORT, BAUD_RATE)
    arduino.write('1')
    print arduino.read()
