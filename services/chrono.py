#!/usr/bin/env python
import sys
sys.path.insert(0, '../driver')

from   time import sleep
import arrow
from   display import Display

class Chrono():

    def __init__(self):
        self.start()

    def start(self):
        self.start = arrow.now()

    def get_elapsed(self):
        end   = arrow.now()
        delta = end - self.start
        dmins, dsecs = divmod(delta.total_seconds(), 60)
        dhrs, dmins  = divmod(dmins, 60)
        return '{:02d}:{:02d}:{:02d}'.format(int(dhrs), int(dmins), int(dsecs))

if __name__ == '__main__':
    dis = Display('/dev/tty.SLAB_USBtoUART')
    chrono = Chrono()
    while True:
        td = chrono.get_elapsed()
        print (td)
        dis.simple_static_message(td)
        sleep(1)
