#!/usr/bin/python
import cgi
import cgitb
import LEDManager

cgitb.enable()  # Per debuggare eccezioni a video

fs = cgi.FieldStorage()

print("Content-Type: text/plain;charset=utf-8")
print()

print("--- Led Controller ---")

print()

print("Keys: " + str(fs.keys()))
print()

print("Key[0]: " + str(fs.keys()[0]))
print("Key[1]: " + str(fs.keys()[1]))
print("Key[2]: " + str(fs.keys()[2]))
print()

action = str(fs["action"].value)
pin = int(fs["pin"].value)
delay = int(fs["delay"].value)

print("---------")

print("action:" + action)
print("delay:" + str(delay))
print("pin:" + str(pin))

print("---------")

if action == 'on':
    print("on action...")
    LEDManager.on(pin, delay)
elif action == 'blink':
    print("blink action...")
    LEDManager.blink(pin, delay)
elif action == "fade":
    print("fade action...")
    LEDManager.fade(pin, delay)


print("---------------")