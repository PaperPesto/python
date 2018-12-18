#!/usr/bin/python
import cgi

fs = cgi.FieldStorage()

print("Content-Type: text/plain;charset=utf-8")
print()

print("Here read-queryparam.py!")

print()
print("------")

print("Keys: " + str(fs.keys()))
print()

print("Key1: " + str(fs.keys()[0]))
print("Key2: " + str(fs.keys()[1]))
print()

print("Value[Key1]: " + str(fs['firstparam'].value))
print("------")