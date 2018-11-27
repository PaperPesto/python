#!/usr/bin/python
import cgi

fs = cgi.FieldStorage()

print("Content-Type: text/plain;charset=utf-8")
print()

print("Hello World from index2.py!")

print(fs.keys())
print(fs.keys()[0])
print(fs['nome'].value)

