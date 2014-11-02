'''
Created on Mar 19, 2014

@author: Python Viet Nam
@Edited: congto
'''
import serial  
import time
def Sending(message, sender):
    SerialPort = serial.Serial("/dev/ttyUSB0",19200)
    SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('AT+CMGS="'+sender+'"\r\n')
    time.sleep(1)
    SerialPort.write(message+"\x1A")
    time.sleep(1)
    print 'Bat dau gui tin, hay kt so dien thoai duoc gui'
    SerialPort.close()
x = raw_input("Ban hay nhap so: \n")
y = raw_input("Ban hay nhap tin nhan: \n")
 
Sending(y,x)