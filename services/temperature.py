#!/usr/bin/env python
import sys
from   time import sleep
import arrow
from sensor.DS18B20 import DS18B20
class Temperature():

    UPDATE_INTERVAL_min = 1

    def __init__(self):
        self.ds = DS18B20('28-000004b422a2')
        self.update()

    def update(self):
        print ('Updating temperature...')
        self.last_update = arrow.now()
        try:
            t  = self.ds.temperature()  # read temperature
            self.current = "Temperature : {} 'C".format(t.C)
        except:
            self.current = 'TEMPERATURE UPDATE ERROR'

    def get_current(self):
        delta = arrow.now() - self.last_update
        if (delta.total_seconds() > (self.UPDATE_INTERVAL_min * 60)):
            self.update()
        return self.current

if __name__ == '__main__':
    temperature = Temperature()
    td = temperature.get_current()
    print (td)
