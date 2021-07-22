#!/bin/python

import socket

## Create new socket
tcpSocketNew = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Set socket options
tcpSocketNew.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

## Bind the socket to network host and port 8000
tcpSocketNew.bind(("0.0.0.0", 8000))

## Make the socket listen
tcpSocketNew.listen(2)

## Use accept
print("Waiting for connection")
(client, ( ip, port)) = tcpSocketNew.accept()

print("Welcome: ", ip)

data = 'lol'

while len(data):

	data = client.recv(2048)
	print("Client sent: " + str(data))
	client.send(data)

print("Closing")
client.close()

print("Server shutdown")
tcpSocket.close()
