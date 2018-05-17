#!/usr/bin/env python
from time import sleep

import arrow


class Chrono:

    def __init__(self):
        self.start = None

    def start(self):
        self.start = arrow.now()

    def get_elapsed(self):
        end = arrow.now()
        delta = end - self.start
        dmins, dsecs = divmod(delta.total_seconds(), 60)
        dhrs, dmins = divmod(dmins, 60)
        return '{:02d}:{:02d}:{:02d}'.format(int(dhrs), int(dmins), int(dsecs))


if __name__ == '__main__':
    chrono = Chrono()
    while True:
        td = chrono.get_elapsed()
        print (td)
        sleep(1)
