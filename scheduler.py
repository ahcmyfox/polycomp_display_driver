#!/usr/bin/env python
import sys
import time
import arrow

sys.path.insert(0, 'services')
sys.path.insert(0, 'services/sentences')
sys.path.insert(0, 'driver')

from display          import Display
from clock            import Clock
from chrono           import Chrono
from countdown        import Countdown
from weather          import Weather
from sentences_server import SentencesServer

def display_clock(display, clock, duration):
    previous = ""
    count    = 0
    while (count < duration):
        time.sleep(0.1)
        message = 'Il est {}'.format(clock.get_now())
        if (message != previous):
            count = count + 1
            previous = message
            print message
            display.simple_static_message(message)

def display_weather(display, weather, duration):
    message = weather.get_current()
    print message
    display.simple_static_message(message)
    time.sleep(duration)

def on_sentences_update(sentences):
    print('sentences updated')
    print(sentences)

def display_sentences(display, server, duration):
    sentences = server.get_sentences()
    print sentences
    if (len(sentences) > 0):
        display.multiple_sliding_message(sentences)
        time.sleep(duration)

if __name__ == '__main__':
	
    display   = Display('/dev/tty.Bluetooth-Incoming-Port')
    clock     = Clock()
    weather   = Weather()
    sentences = SentencesServer(8000, on_sentences_update)

    display.open()
    sentences.start()

    try:
        while (True):
            display_clock(display, clock, 3)
            display_weather(display, weather, 6)
            display_sentences(display, sentences, 30)
    except KeyboardInterrupt:
        print('SigTerm received, shutting down')
        sys.exit(0)



    	
