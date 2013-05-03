#!/usr/bin/env python
# coding: utf-8

import serial
import time

class Arduino(object):
    '''Define a Arduino object.'''
    
    def connect(self, port, baud_rate):
        self.arduino = serial.Serial(port, baud_rate)
        time.sleep(2)

    def write(self, data):
        self.arduino.write(data)

    def read(self):
        return self.arduino.readline()

if __name__ == '__main__':
    arduino = Arduino()
    arduino.connect('/dev/ttyACM0',115200)
    arduino.write('1')
    print arduino.read()

