#!/usr/bin/env python3 
from enum import Enum

class Color(Enum):
    """Just a prebuilt color enum."""
    pre = '\033['
    fg_red = pre + '31m'
    fg_green = pre + '32m'
    fg_cyan = pre + '36m'
    fg_white = pre + '37m'
    fg_yellow = pre + '93m'

    bg_red = pre + '41m'
    bg_green = pre + '42m'
    bg_cyan = pre + '46m'

    bold = pre + '1m'
    bln = pre + '5m'
    underline = pre + '4m'
    reset = pre + '0m'


def full_color_print(msg):
    if msg.startswith('[+]'):
        print(Color.fg_green.value + msg + Color.reset.value)
    elif msg.startswith('[-]'):
        print(Color.fg_red.value + msg + Color.reset.value)
    elif msg.startswith('[*]'):
        print(Color.fg_yellow.value + msg + Color.reset.value)
    elif msg.startswith('[!]'):
        print(Color.fg_white.value + Color.bg_red.value + Color.bln.value + msg + Color.reset.value)
    elif msg.startswith('DEBUG:'):
        print(Color.fg_cyan.value + msg + Color.reset.value)
    else:
        print(msg)
    return

def word_label_color_print(msg):
    if msg.startswith('[OK]'):
        print('[' + Color.fg_green.value +'OK'+ Color.reset.value + ']' + msg.partition(']')[-1])
    elif msg.startswith('[FAIL]'):
        print('[' + Color.fg_red.value +'FAIL'+ Color.reset.value + ']' + msg.partition(']')[-1])
    elif msg.startswith('[INFO]'):
        print('[' + Color.fg_yellow.value +'INFO'+ Color.reset.value + ']' + msg.partition(']')[-1])
    elif msg.startswith('[WARN]'):
        print('[' + Color.fg_white.value + Color.bg_red.value +'WARN'+ Color.reset.value + ']' + msg.partition(']')[-1])
    elif msg.startswith('[DEBUG]'):
        print('[' + Color.fg_cyan.value +'DEBUG'+ Color.reset.value + ']' + msg.partition(']')[-1])
    else:
        print(msg)
    return

def label_color_print(msg):
    if msg.startswith('[+]'):
        print('[' + Color.fg_green.value +'+'+ Color.reset.value + ']' + msg.partition(']')[-1])
    elif msg.startswith('[-]'):
        print('[' + Color.fg_red.value +'-'+ Color.reset.value + ']' + msg.partition(']')[-1])
    elif msg.startswith('[*]'):
        print('[' + Color.fg_yellow.value +'*'+ Color.reset.value + ']' + msg.partition(']')[-1])
    elif msg.startswith('[!]'):
        print('[' + Color.fg_red.value +'!'+ Color.reset.value + ']' + Color.fg_white.value + Color.bg_red.value + msg.partition(']')[-1])
    elif msg.startswith('[D]'):
        print('[' + Color.fg_cyan.value +'D'+ Color.reset.value + ']' + msg.partition(']')[-1])
    else:
        print(msg)
    return


