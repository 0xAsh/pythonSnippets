# Reads /var/log/messages.log and looks for logs containing usb info.
# Super simple just to get familiar with interacting with files via Python.
# Why not just use grep though?

#!/bin/python

file = open("/var/log/messages.log", "r")
for line in file:
	if "usb" in line:
		print(line.strip())

file.close()
