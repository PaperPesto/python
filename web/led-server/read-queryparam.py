#!/usr/bin/python
import cgi

fs = cgi.FieldStorage()

print("Content-Type: text/plain;charset=utf-8")
#!/usr/bin/python
import cgi

fs = cgi.FieldStorage()

print("Content-Type: text/plain;charset=utf-8")
print()

print("Here read-queryparam.py!")

print()
print("------")

print("fs.keys(): " + str(fs.keys()))
print()

print("fs.keys()[0]: " + str(fs.keys()[0]))
print()

print("fs['firstparam'].value: " + str(fs['firstparam'].value))
print("------")