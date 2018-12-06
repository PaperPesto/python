from gpiozero import LED
from time import sleep


def on(ledpin):
    led = LED(ledpin)
    led.on()

def off(ledpin):
    led = LED(ledpin)
    led.off()

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Dice Manager module, type help as argument")
    elif len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            print("Usage: $ python led-manager.py <arg1> <arg2>")
        else:
            ledpin = int(sys.argv[1])
            print("led ", str(ledpin))
            action = sys.argv[2]
            print("action:", action)
            if action == 'on':
                print("Executing action on...")
                on(ledpin)
            elif action == 'off':
                print("Executing action off...")
                off(ledpin)