from time import sleep

import serial

from protocol import Protocol


class Display:
    addr = 1;

    def __init__(self, port):
        self.ser = serial.Serial(self.port,
                                 baudrate=9600,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS,
                                 writeTimeout=0,
                                 timeout=10,
                                 rtscts=False,
                                 dsrdtr=False,
                                 xonxoff=False)
        self.port = port

    def open(self):
        self.ser.flushInput()
        self.ser.flushOutput()
        print "Opening serial port " + self.ser.name  # check which port was really used

    def time_message(self):
        buf = Protocol.build_frame(Protocol.mk_header(addr=self.addr), Protocol.mk_serst(), Protocol.mk_page(time=True))
        self.send(buf)

    def alert_message(self, message):
        buf = Protocol.build_frame(Protocol.mk_header(addr=self.addr), Protocol.mk_serst(),
                                   Protocol.mk_page(msg=message, cmd='FLASH'))
        self.send(buf)

    def simple_static_message(self, message):
        buf = Protocol.build_frame(Protocol.mk_header(addr=self.addr), Protocol.mk_serst(),
                                   Protocol.mk_page(msg=message, effect='APPEAR'))
        self.send(buf)

    def simple_sliding_message(self, message):
        buf = Protocol.build_frame(Protocol.mk_header(addr=self.addr), Protocol.mk_serst(),
                                   Protocol.mk_page(msg=message, effect='SLIDE'))
        self.send(buf)

    def mk_multiple_messages(self, effect, messages, delay):
        buf = ""
        i = 1
        for message in messages:
            if i < (len(messages)):
                trame = Protocol.build_frame(Protocol.mk_header(addr=self.addr),
                                             Protocol.mk_serst(more=True),
                                             Protocol.mk_page(msg=message, num='00' + str(i), persist_time=delay,
                                                              last=False, effect=effect))
            else:
                trame = Protocol.build_frame(Protocol.mk_header(addr=self.addr),
                                             Protocol.mk_serst(more=False),
                                             Protocol.mk_page(msg=message, num='00' + str(i), persist_time=delay,
                                                              last=True, effect=effect))
            print trame.encode("hex")
            self.send(trame)
            sleep(0.1)
            i = i + 1
        return buf

    def multiple_static_message(self, messages, delay='S2', effect='APPEAR'):
        buf = self.mk_multiple_messages(effect, messages, delay)

    def multiple_sliding_message(self, messages, delay='S10'):
        buf = self.mk_multiple_messages('SLIDE', messages, delay)

    def close(self):
        self.ser.close()

    def send(self, buf):
        print "Sending " + buf.encode("hex")
        self.open()
        self.ser.write(buf)
        self.close()


def display_test():
    dis = Display('/dev/ttyUSB0')
    # dis.simple_static_message("Simple static")
    # dis.time_message()
    dis.alert_message("SE-RE-NI-TE")
    # dis.simple_sliding_message("Simple sliding")
    # dis.multiple_static_message(["aaa", "bbb", "ccc", "ddd", "eee", "fff"], 'S2')
    # dis.multiple_sliding_message(["Multiple", "sliding", "messages"], 'S10')


if __name__ == "__main__":
    display_test()
