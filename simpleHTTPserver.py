#!/bin/python

import socketserver
import http.server

## Create a handler to overwrite the default GET handler

class HttpRequestHandler (http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/admin':
			self.wfile.write('What are you doing?')
			self.wfile.write(self.headers)

		else:
			http.server.SimpleHTTPRequestHandler.do_GET(self)

## Create a handler to overwrite the default GET handle
httpServer = socketserver.TCPServer(('', 10001), http.server.SimpleHTTPRequestHandler)

httpServer.serve_forever()
