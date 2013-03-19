# Download and parser system
# Steam Stats

import requests
import xml.etree.ElementTree as ET

class ConnectError(Exception):
	pass

def Download(Link=None):

	filename = os.path("tmp/temp.xml")

	try:
		r = requests.get(Link)
	except:
		raise ConnectError

	if r.status_code in (404, 500, 503):
		raise ConnectError
	else:
		pass

	with open(filename, "wb") as code:
		code.write(r.content)

	tree = ET.parse(filename)	
	root = tree.getroot()
	os.remove(filename)

	return root