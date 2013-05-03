#!/usr/bin/env python
# coding: utf-8

import serial
import time
import glob

class Arduino(object):
    '''Defines a Arduino object.'''

    def connect(self, port, baud_rate):
        self.arduino = serial.Serial(port, baud_rate)
        time.sleep(2)

    def write(self, data):
        self.arduino.write(data)

    def read(self):
        return self.arduino.readline()
   
if __name__ == '__main__':
    
    SERIAL_PORT = '/dev/ttyACM*'

    arduino = Arduino()
    available_ports = glob.glob(SERIAL_PORT)
    if not available_ports:
        print 'Arduino not found'
        time.sleep(1)
    else:
        arduino_filename = available_ports[0]
        try:
            arduino.connect(arduino_filename, 115200)
            arduino.write('1')
            print arduino.read()
        except serial.serialutil.SerialException:
            print 'Serial exception'
            time.sleep(1)

