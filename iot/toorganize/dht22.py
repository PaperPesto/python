import Adafruit_DHT as dht    # Importing Adafruit library for DHT22
from time import sleep           # Impoting sleep from time library to add delay
print("starting")
try:
    while True:                # Loop will run forever
        humi, temp = dht.read_retry(dht.DHT22, 21)  # Reading humidity and temperature
        print ('Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(temp, humi)) 
	print ('hello')
        sleep(3)
# If keyboard Interrupt is pressed
except KeyboardInterrupt:
    pass  			# Go to next line
