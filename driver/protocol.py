import construct as cst

con = cst.Container  # alias

# header
# pkt_header = bytearray([0x00, # header sync
#                         0x01, # lines (=1)
#                         0x01, # sign address
#                         0x03, # etx - end of header
#                     ])

# #msg_prefix = bytearray("\xC8001\xEF\xC1\x80")
# def build_prefix(func=1, speed=15):
#     msg_prefix = bytearray([
#         0xc8,#0b11000000, # serial status flags (orig. 0xc8)
#         0x30, # page (0xx)
#         0x30, # page (x0x)
#         0x31, # page (xx1) = 001
#         0b11000000 | speed, # ? # tempo
#         0xc0 | (func & 0x0f), # ? # function = paint
#         0x80, # ? # page status
#     ])
#     return msg_prefix

# flags = 0b1100 1000
# --------
# :0, :5 = 0
# :6, :7 = 1
# 0b110x xxx0
# :1 = interrupt mode
# :2 = more pages to follow flag (clear = no more pages)
# :3 = ack requested
# :4 = schedule mode (clear = no schedule)
# 0b11001010

# tempo
# -----
# 0b11xx xxxx

# function
# --------
# 0b11aa bbbb
# :5 = show temp
# :4 = show time
# :0 - :3
# 0 = random
# 1 = appears
# 2 = wipe
# 3 = open
# 4 = lock
# 5 = rotate
# 6 = right
# 7 = left
# 8 = roll up
# 9 = roll dn
# 10= ping pong
# 11= fill up
# 12= paint
# 13= fade in
# 14= jump
# 15= slide

# page status
# -----------
# 0x80 = 0b10000000
# :7 always set, rest clear.


# msg_suffix = bytearray([0x04]) # EOT - end of text/packet.

# def construct_message(msg):
#     msgbuf = pkt_header + build_prefix(15, 3) + bytearray(msg) + msg_suffix
#     checksum = build_checksum(msgbuf)
#     msgbuf += bytearray([checksum])
#     return str(msgbuf)

# def build_checksum(buf):
#     chk = 0
#     for c in buf:
#         chk ^= c
#     return chk

HEADER = cst.Struct('pc_header',
                    cst.Magic('\x00'),
                    cst.Const(cst.UBInt8('lines'), 1),
                    cst.UBInt8('address'),
                    cst.Magic('\x03'))

SER_STATUS = cst.BitStruct('serst',
                           cst.Magic('\x01\x01\x00'),
                           cst.Flag('schedule_enabled'),
                           cst.Flag('ack_enabled'),
                           cst.Flag('further_pages'),
                           cst.Flag('interrupt_mode'),
                           cst.Magic('\x00'))

PAGE_IDX = cst.Bytes('page_num', 3)

TEMPO = cst.BitStruct('tempo',
                      cst.Magic('\x01\x01'),
                      cst.Enum(cst.BitField('display_ctrl', 2),
                               TIMED=0, FIXED_ON=1, FIXED_OFF=2),
                      cst.Enum(cst.BitField('persist_time', 4),
                               S2=1, S5=2, S10=3, S20=4, S30=5,
                               S45=6, S60=7, S90=8, S120=9))

# TODO: union persist_time with scroll_speed

PAGE_FUNC = cst.BitStruct('page_func',
                          cst.Magic('\x01\x01'),
                          cst.Flag('show_temp'),
                          cst.Flag('show_time'),
                          cst.Enum(cst.BitField('page_effect', 4),
                                   RANDOM=0,
                                   APPEAR=1,
                                   WIPE=2,
                                   OPEN=3,
                                   LOCK=4,
                                   ROTATE=5,
                                   RIGHT=6,
                                   LEFT=7,
                                   ROLL_UP=8,
                                   ROLL_DOWN=9,
                                   PINGPONG=10,
                                   FILL_UP=11,
                                   PAINT=12,
                                   FADE_IN=13,
                                   JUMP=14,
                                   SLIDE=15))

PAGE_CFG = cst.BitStruct('page_cfg',
                         cst.Magic('\x01'),
                         cst.Flag('background_on'),
                         cst.Flag('non_english'),
                         cst.Flag('autocenter'),
                         cst.Flag('bold_joins_78'),
                         cst.Flag('bold_joins_56'),
                         cst.Flag('bold_joins_34'),
                         cst.Flag('bold_joins_12'),
                         )

CMD_SEQ = cst.Struct('_cmd',
                     cst.Magic('\x1c'),
                     cst.Enum(cst.Byte('cmd'),
                              FLASH=70,
                              ENLARGE=69,
                              DEFAULT=68))

PAGE = cst.Struct('page',
                  PAGE_IDX,
                  cst.Embed(TEMPO),
                  cst.Embed(PAGE_FUNC),
                  cst.Embed(PAGE_CFG),
                  cst.Embed(CMD_SEQ),
                  cst.CString('body', terminators='\x04'))

DATETIME_BODY = cst.Struct('datetime_page',
                           cst.Const(PAGE_IDX, '000'),

                           )
# values as ascii numbers 0x30-0x39

MESSAGE = cst.Struct('msg', HEADER, SER_STATUS, PAGE)


class Protocol:
    def __init__(self):
        pass

    @staticmethod
    def datetime_page():
        pass

    @staticmethod
    def mk_header(addr=1):
        return con(address=addr, lines=1)

    @staticmethod
    def mk_serst(sched=False, ack=False, more=False, intr=False):
        return con(schedule_enabled=sched,
                   ack_enabled=ack,
                   further_pages=more,
                   interrupt_mode=intr)

    @staticmethod
    def mk_page(msg='', effect='APPEAR', num='001', persist_time='S60', cmd='DEFAULT', last=True, center=True,
                time=False):
        return con(page_num=num,
                   display_ctrl='TIMED',
                   persist_time=persist_time,
                   show_temp=False,
                   show_time=time,
                   page_effect=effect,
                   background_on=False,
                   non_english=False,
                   autocenter=center,
                   bold_joins_78=False,
                   bold_joins_56=False,
                   bold_joins_34=False,
                   bold_joins_12=False,
                   cmd=cmd,
                   body=msg)

    @staticmethod
    def build_checksum(buf):
        chk = 0
        for c in buf:
            chk ^= c
        return chk

    @staticmethod
    def build_frame(header, serst, page):
        c = con(pc_header=header,
                serst=serst,
                page=page
                )
        ba_packet = bytearray(MESSAGE.build(c))
        ck = Protocol.build_checksum(ba_packet)
        ba_packet.append(ck)
        return str(ba_packet)
