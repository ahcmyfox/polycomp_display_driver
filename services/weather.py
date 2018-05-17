#!/usr/bin/env python

import json
import urllib2

import arrow


class Weather:
    UPDATE_INTERVAL_min = 15

    def __init__(self):
        self.url = "http://www.prevision-meteo.ch/services/json/lat=43.535lng=1.517"
        self.update()
        self.last_update = arrow.now()
        self.current = ''

    def update(self):
        print ('Updating weather...')
        try:
            jsonstr = urllib2.urlopen(self.url).read()
            content = json.loads(jsonstr)
            curr = content['current_condition']
            self.current = '{}  - {}\'C - {}km/h {} (raf {}km/h)'.format(curr['condition_key'],
                                                                         curr['tmp'],
                                                                         curr['wnd_spd'],
                                                                         curr['wnd_dir'],
                                                                         curr['wnd_gust'])
        except:
            self.current = 'WEATHER UPDATE ERROR'

    def get_current(self):
        delta = arrow.now() - self.last_update
        if delta.total_seconds() > (self.UPDATE_INTERVAL_min * 60):
            self.update()
        return self.current


if __name__ == '__main__':
    weather = Weather()
    td = weather.get_current()
    print (td)
