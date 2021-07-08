#!/bin/python

import os
import time

def child_process():
	print("I am the child, here is my PID: " + str(os.getpid()))

	print("exiting")

def parent_process():
	print("I am the parent process, here is my PID: " + str(os.getpid()))

	## Creates a new process
	## os.fork when called inside the parent process returns the PID of the child
	## when os.fork is called inside a child process it returns 0
	childPID = os.fork()
	print(childPID)
	if childPID == 0:
		# we are inside the child
		child_process()
	else:
		# we are inside the parent process
		print("we're inside the parent EWWW")
		print("Our child has the PID: " + str(childPID))

parent_process()


time.sleep(10)
