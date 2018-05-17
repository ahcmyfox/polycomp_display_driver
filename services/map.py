#!/usr/bin/env python

import json
import time
import urllib2

import arrow


class Map:
    UPDATE_INTERVAL_min = 10

    def __init__(self):
        self.current = 'MAP UPDATE ERROR'
        self.last_update = arrow.now()
        self.url_format = 'https://maps.googleapis.com/maps/api/directions/json?origin=place_id:ChIJuUAJHRy-rhIRFaUq8ZsWn_s&destination=43.558010,1.492678&departure_time={}&key=AIzaSyCJUp4B42mhuc1XMWE0fcJJbUGndPyCPMI'
        self.update()

    def update(self):
        print ('Updating map...')
        try:
            epoch_time = int(time.time())
            url = self.url_format.format(epoch_time)
            jsonstr = urllib2.urlopen(url).read()
            content = json.loads(jsonstr)
            duration = content['routes'][0]['legs'][0]['duration_in_traffic']['text']
            self.current = 'Sortie de Labege : {}'.format(duration)
        except:
            pass

    def get_current(self):
        delta = arrow.now() - self.last_update
        if delta.total_seconds() > (self.UPDATE_INTERVAL_min * 60):
            self.update()
        return self.current


if __name__ == '__main__':
    map = Map()
    duration = map.get_current()
    print (duration)
