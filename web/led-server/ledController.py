#!/usr/bin/python
import cgi
import LEDManager

fs = cgi.FieldStorage()

print("Content-Type: text/plain;charset=utf-8")
print()

print("--- Led Controller ---")

print()
print("------")

print("Keys: " + str(fs.keys()))
print()

print("Key[0]: " + str(fs.keys()[0]))
print("Key[1]: " + str(fs.keys()[1]))
print("Key[2]: " + str(fs.keys()[2]))
print()

print("Value[Key[0]]: " + str(fs[fs.keys()[0]].value))
print("Value[Key[1]]: " + str(fs[fs.keys()[1]].value))
print("Value[Key[2]]: " + str(fs[fs.keys()[2]].value))

action = str(fs.keys()[0])
delay = int(fs.keys()[1])
pin = int(fs.keys()[2])

print("action:" + action)
print("delay:" + delay)
print("pin:" + pin)

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

