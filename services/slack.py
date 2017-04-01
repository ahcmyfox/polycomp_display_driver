import sys
import urllib2
from   time import sleep
import json

class Slack():

    def __init__(self):
    	self.url = "http://stackoverflow.com/questions/28364083/simplehttpserver-launched-as-a-thread-does-not-daemonize"

    def serialize(self, content):
        if(len(decoded['messages']) > 0):
            return decoded['messages'][0]['user'] + " : " + decoded['messages'][0]['message']
        else:
            return False

    def get(self):
    	try:
            jsonstr = urllib2.urlopen(self.url).read()
            decoded = json.loads(jsonstr)
            return self.serialize(decoded)
        except:
        	return False

if __name__ == "__main__":
    slack = Slack()
    while True:
        ret = slack.get()
        if (ret != False):
            print ret
        else:
            print "(error)"
        sleep(1)
		