#!/usr/bin/env python
from time import sleep
import arrow
from display import Display

def fmt_timedelta(start, end=None):
    if end is None:
        end = arrow.now()
    delta = end - start
    dmins, dsecs = divmod(delta.total_seconds(), 60)
    dhrs, dmins  = divmod(dmins, 60)
    return '{:02d}:{:02d}:{:02d}'.format(int(dhrs), int(dmins), int(dsecs))

def run():
    dis = Display()
    start_time = arrow.now()
    while True:
        td = fmt_timedelta(start=start_time)
        print td
        dis.simple_static_message(td)
        sleep(1)

if __name__ == '__main__':
    run()
