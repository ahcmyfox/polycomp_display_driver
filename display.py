import serial
from protocol import Protocol
from time import sleep

class Display():

    def open(self):
        self.addr = 1
        self.port = '/dev/tty.usbserial-FT8WJS9S'
        self.ser = serial.Serial(self.port,
                                 baudrate=9600,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE,
                                 bytesize=serial.EIGHTBITS,
                                 writeTimeout = 0,
                                 timeout = 10,
                                 rtscts=False,
                                 dsrdtr=False,
                                 xonxoff=False)
        self.ser.flushInput()
        self.ser.flushOutput()
        print "Opening serial port " + self.ser.name         # check which port was really used

    def alert_message(self, message):
        self.multiple_static_message([message, ' '], 'S2')

    def simple_static_message(self, message):
        self.open()
        buf = Protocol.build_frame(Protocol.mk_header(addr=self.addr), Protocol.mk_serst(), Protocol.mk_page(msg=message, effect = 'APPEAR'))
        self.send(buf)

    def simple_sliding_message(self, message):
        self.multiple_sliding_message([message], 'S2')

    def mk_multiple_messages(self, effect, messages, delay):
        buf = ""
        i = 1
        for message in messages:
            if(i<len(messages)):
                trame = Protocol.build_frame(Protocol.mk_header(addr=self.addr), 
                                                 Protocol.mk_serst(more=True),  
                                                 Protocol.mk_page(msg=message, num = '00' + str(i), persist_time = delay, last = False, effect = effect))
            else:
                print 'last'
                trame = Protocol.build_frame(Protocol.mk_header(addr=self.addr), 
                                                 Protocol.mk_serst(more=False), 
                                                 Protocol.mk_page(msg=message, num = '00' + str(i), persist_time= delay, last = True, effect = effect))
            print trame.encode("hex")
            buf = buf + trame
            i = i + 1
        return buf

    def multiple_static_message(self, messages, delay):
        self.open()
        buf = self.mk_multiple_messages('APPEAR', messages, delay)
        self.send(buf)    

    def multiple_sliding_message(self, messages, delay):
        self.open()
        buf = self.mk_multiple_messages('SLIDE', messages, delay)
        self.send(buf)

    def close(self):
        self.ser.close()

    def send(self, buf):
        print "Sending " + buf.encode("hex")
        self.ser.write(buf)
        self.close()

def display_test():
    dis = Display()
    #dis.simple_static_message("Simple static")
    #dis.alert_message("Alert")
    dis.simple_sliding_message("Simple sliding")
    #dis.multiple_static_message(["Multiple", "static", "messages"], 'S2')
    #dis.multiple_sliding_message(["Multiple", "sliding", "messages"], 'S10')

if __name__ == "__main__":
    display_test()
 