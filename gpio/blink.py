from gpiozero import LED
from time import sleep

led = LED(17)
while True:
    led.on()
    print("led on")
    sleep(0.5)
    print("led off")
    led.off()
    sleep(0.5)
