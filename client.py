import os
import sys
import base64
import requests

API_ENDPOINT = 'http://localhost:8001/'

f = open(os.ttyname(0))

method = 'POST'
if len(sys.argv) > 1 and sys.argv[1] == 'GET':
	print "Selected method GET"
	method = 'GET'

while 1:
	sys.stdout.write('$ ')
	line = f.readline().strip()
	
	# stop the loop if no line was read
	if not line:
		break
	
	payload = {'command': base64.b64encode(line)}
	
	if method == 'POST':
		r = requests.post(url = API_ENDPOINT, data = payload)
	else:
		r = requests.get(url = API_ENDPOINT, params = payload)
	
	print base64.b64decode(r.text)

f.close()
