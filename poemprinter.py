#!/usr/bin/env python
	 
import os
from time import sleep	 
import RPi.GPIO as GPIO
	 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #button 1
GPIO.setup(24, GPIO.IN) #button 2

GPIO.setup(17,GPIO.OUT) #LED for button 1
GPIO.setup(27,GPIO.OUT) #LED for button 2

os.system('sudo chown pi:pi /dev/usb/lp0')

while True:
	GPIO.output(17, GPIO.HIGH)
	GPIO.output(27, GPIO.HIGH)
	
	if (GPIO.input(23) == False):
		os.system('sh /home/pi/Desktop/PocketPoems/startup')
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		sleep(10);
		
	if (GPIO.input(24) == False):
		os.system('sh /home/pi/Desktop/PocketPoems/startup')
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		sleep(10);