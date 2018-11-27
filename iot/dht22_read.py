import Adafruit_DHT as dht    # Importing Adafruit library for DHT22
from time import sleep           # Impoting sleep from time library to add delay
print("starting...")

try:
    while True:                # Loop will run forever
        # Reading humidity and temp
        humi, temp = dht.read_retry(dht.DHT22, 21)
        print('Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(temp, humi))
        sleep(3)

# If keyboard Interrupt is pressed
except KeyboardInterrupt:
    pass                        # Go to next line
