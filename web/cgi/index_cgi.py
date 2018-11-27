#!/usr/bin/python
# Tirare su Apache2 2 configurarlo con il tutorial https://www.digitalocean.com/community/tutorials/how-to-set-up-an-apache-mysql-and-python-lamp-server-without-frameworks-on-ubuntu-14-04
import cgi

fs = cgi.FieldStorage()

print("Content-Type: text/plain;charset=utf-8")
print()

print("Hello World from index2.py!")

print(fs.keys())
print(fs.keys()[0])
print(fs['nome'].value)
