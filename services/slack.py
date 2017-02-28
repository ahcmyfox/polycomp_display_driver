import sys
sys.path.insert(0, '../driver')

import urllib2
from   time import sleep
from   display import Display
import json

if __name__ == "__main__":
	dis = Display('COM7')
	while True:
		jsonstr = urllib2.urlopen("http://api-dev.myfox.io:7777/read").read()
		print jsonstr
		decoded = json.loads(jsonstr)
		message = ""
		if(len(decoded['messages']) > 0):
			message = decoded['messages'][0]['user'] + " : " + decoded['messages'][0]['message']
			print message
			dis.simple_sliding_message(message)
		sleep(1)