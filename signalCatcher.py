#!/bin/python

import signal
import time

# frame and frm both work IDK why. Maybe it doesn't matter.
# Catches CTRL + C
def signal_handler(signum, frm):
	print("You can't kill the process")

# Catches CTRL + Z
def exit_handler(signum, frm):
	print("Exiting...")
	exit(0)

# Register our signal handler with `SIGINT`(CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Register the exit handler with `SIGTSTP` (Ctrl + Z)
signal.signal(signal.SIGTSTP, exit_handler)




print("Done")

while 1:
	print("Press Ctrl + C")
	time.sleep(1)
