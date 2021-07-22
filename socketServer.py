#!/bin/python

import socketserver

class EchoHandler(socketserver.BaseRequestHandler):
	def handle(self):

		print("Got connection from: " + str(self.client_address))
		data = 'dummy'

		while len(data):
			data = self.request.recv(1024)
			self.request.send(data)

		print("Client left")


## Server setup
serverAddr = ("0.0.0.0", 8000)

server = socketserver.TCPServer(serverAddr, EchoHandler)

server.serve_forever()
