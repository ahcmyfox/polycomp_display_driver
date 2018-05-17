#!/usr/bin/env python
from time import sleep

import arrow


class Clock:

    def __init__(self):
        pass

    @staticmethod
    def get_now():
        return arrow.now().format('HH:mm:ss')


if __name__ == '__main__':
    clock = Clock()
    while True:
        td = clock.get_now()
        print (td)
        sleep(1)
