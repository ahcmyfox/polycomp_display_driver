#!/usr/bin/env python
import sys
from   time import sleep
import arrow

class Clock():

    def get_now(self):
        return arrow.now().format('HH:mm:ss')

if __name__ == '__main__':
    clock = Clock()
    while True:
        td = clock.get_now()
        print (td)
        sleep(1)
