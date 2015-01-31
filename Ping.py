from http.client import HTTPSConnection
from base64 import b64encode

def ping():
	connection	 = HTTPSConnection("173.37.40.112")

	usernamepassword = b64encode(b"ucsbhack5:ucsbhack5").decode("ascii")
	headers = {'Authorization':'Basic %s' % usernamepassword}

	connection.request('GET', '/api/location/v2/clients', headers=headers)
	data = connection.getresponse().read()
	return data