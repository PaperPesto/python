#!/usr/bin/python
import RPi.GPIO as GPIO  
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  

BTN_PIN = 17

# setting inputs
GPIO.setup(BTN_PIN, GPIO.IN)

# this runs when a change of state happens on pin 18
# non blocking
def btn_callback(channel):  
	if GPIO.input(BTN_PIN):
		# execute python code...
		# you can do many exciting things here, like:
		# control outputs of the pi,driving other circuits
		# turning something on/off, play some music...
		print("Button was pressed.")

raw_input("Press Enter when ready\n>")  

# this sets interrupt detection on both falling and rising edges of pin 18 (the button)
# software bounce of 100 millisecond
GPIO.add_event_detect(BTN_PIN, GPIO.BOTH, callback=btn_callback, bouncetime=100)  

try:  
	# this is actually the running program, just blocking.
	while True:
		print("hello diocane!")
		time.sleep(1)
		
except KeyboardInterrupt:  
	GPIO.cleanup()
	
GPIO.cleanup()
