#!/usr/bin/env python
import sys
from   time import sleep
import arrow

class Countdown():

    def start(self, duration):
        self.end = arrow.get(arrow.now().timestamp + duration)

    def get_remaining(self):
        delta = self.end - arrow.now()
        if (delta.total_seconds() > 0):
            dmins, dsecs = divmod(delta.total_seconds() + 1, 60)
            dhrs, dmins  = divmod(dmins, 60)
            return '{:02d}:{:02d}:{:02d}'.format(int(dhrs), int(dmins), int(dsecs))
        else:
            return 'FINISHED'

if __name__ == '__main__':
    countdown = Countdown()
    countdown.start(10)
    while True:
        td = countdown.get_remaining()
        print (td)
        sleep(1)
