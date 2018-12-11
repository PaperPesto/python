# Non è possibile accendere indefinitamente un led con gpiozero
# Ad esempio lo accendo, ritorno il controllo al controller e aspetto un altro handler, lo spengo, ecc
# posso solo accenderlo per tot secondi, spengerlo e poi ritornare al controller

from gpiozero import LED
from time import sleep


def on(ledpin, delay):
    action = "on"
    print("Turning {action} led {pin} for {delay} seconds...".format(action=action, pin=ledpin, delay=delay))
    led = LED(ledpin)
    led.on()
    sleep(delay)


def off(ledpin, delay):
    action = "off"
    print("Turning {action} led {pin} for {delay} seconds...".format(action=action, pin=ledpin, delay=delay))
    led = LED(ledpin)
    led.off()
    sleep(delay)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("LEDManager module, type help as argument")
    elif len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            print("Usage: $ python LEDManager.py <arg1> <arg2> <arg3>")
            print("<arg1>: led")
            print("<arg2>: action")
            print("<arg3>: delay")
        else:
            # Argomenti passati -----
            ledpin = int(sys.argv[1])
            print("led:", str(ledpin))
            action = sys.argv[2]
            print("action:", action)
            delay = int(sys.argv[3])
            print("delay:", delay)

            if action == 'on':
                on(ledpin, delay)
            elif action == 'off':
                off(ledpin, delay)
