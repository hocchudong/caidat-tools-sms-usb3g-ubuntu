#!/usr/bin/python
'''
Script Send SMS on Ubuntu
Edit: ducnc
pythonvietnam.info
'''
import argparse
import serial
import time

parser = argparse.ArgumentParser(description='Send SMS by python')
parser.add_argument('info',nargs=2,help='Please use the following command: python python-sms-cli.py phone_number "Message"')
args = parser.parse_args()

def Sending(message, sender):
    SerialPort = serial.Serial("/dev/ttyUSB0",19200)
    SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('AT+CMGS="'+sender+'"\r\n')
    time.sleep(1)
    SerialPort.write(message+"\x1A")
    time.sleep(1)
    SerialPort.close()

Sending(args.info[1],args.info[0])