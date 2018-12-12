# Non è possibile accendere indefinitamente un led con gpiozero
# Ad esempio lo accendo, ritorno il controllo al controller e aspetto un altro handler, lo spengo, ecc
# posso solo accenderlo per tot secondi, spengerlo e poi ritornare al controller

from gpiozero import LED, PWMLED
from time import sleep

actions = ['on', 'blink', 'pulse']

def on(ledpin, delay):
    '''Accende il led'''
    action = actions[0]
    print("{action} led {pin} for {delay} seconds...".format(action=action, pin=ledpin, delay=delay))
    led = LED(ledpin)
    led.on()
    sleep(delay)

def blink(ledpin, delay):
    '''Accende ad intermittenza il led'''
    action = actions[1]
    print("{action} led {pin} for {delay} seconds...".format(action=action, pin=ledpin, delay=delay))
    led = LED(ledpin)
    led.blink()
    sleep(delay)

def fade(ledpin, delay):
    '''Accende il led con fade in/out'''
    action = actions[2]
    print("{action} led {pin} for {delay} seconds...".format(action=action, pin=ledpin, delay=delay))
    led = PWMLED(ledpin)
    led.pulse()
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

            if action == actions[0]:
                on(ledpin, delay)
            elif action == actions[1]:
                blink(ledpin, delay)
            elif action == actions[2]:
                fade(ledpin, delay)
