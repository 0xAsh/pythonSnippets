#!/bin/python

# So the python 3 thread module has an underscore before it for some fucking reason
# The examples in the course use just "thread" with python2
import _thread
import time

def worker_thread(id):

	print("Thread ID %d now alive" % id)
	count = 1
	while count < 5:
		print("Thread with ID " + str(id) + " has counter value " + str(count))
		time.sleep(2)
		count += 1

for i in range(5):
	# First argument in start_new_thread is the name of the function you want to call
	# Second input is arguments you want to pass to the worker thread, in the form of a tuple
	_thread.start_new_thread(worker_thread, (i,))

print("Main thread going for an infitie wait loop")
while True:
	pass
