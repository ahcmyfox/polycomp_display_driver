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
from saints           import Saints

def display_sliding_and_delay(display, message):
    display.simple_sliding_message(message)
    time.sleep(0.121 * len(message) + 2.3)

def display_clock(display, clock, duration):
    previous = ""
    count    = 0
    while (count < duration):
        message = 'Il est {}'.format(clock.get_now())
        if (message != previous):
            count = count + 1
            previous = message
            print message
            display.simple_static_message(message)

def display_weather(display, weather):
    message = weather.get_current()
    print message
    display_sliding_and_delay(display, message)

def display_saint(display, saints):
    message = saints.get_current()
    print message
    display_sliding_and_delay(display, message)

def on_sentences_update(sentences):
    print('sentences updated')
    print(sentences)

def display_sentences(display, server):
    sentences = server.get_sentences()
    print sentences
    for i in range(len(sentences)):
        display_sliding_and_delay(display, sentences[i])
        display_clock(display, clock, 6)

if __name__ == '__main__':
	
    display   = Display('/dev/ttyUSB0')
    clock     = Clock()
    weather   = Weather()
    saints    = Saints()
    sentences = SentencesServer(8000, on_sentences_update)

    display.open()
    sentences.start()

    try:
        while (True):
            display_clock(display, clock, 6)
            display_weather(display, weather)
            display_clock(display, clock, 6)
            display_saint(display, saints)
            display_clock(display, clock, 6)
            display_sentences(display, sentences)
    except KeyboardInterrupt:
        print('SigTerm received, shutting down')
        sys.exit(0)



    	
