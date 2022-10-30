#!/usr/bin/env python3 
import logging
class Color:
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
    format = '%(asctime)s %(levelname)s - %(filename)s: %(message)s'


class ColoredFormatter(logging.Formatter):
    FORMATS = {
        logging.INFO: Color.fg_white + Color.format + Color.reset,
        logging.DEBUG: Color.fg_cyan + Color.format + Color.reset,
        logging.WARNING: Color.fg_yellow + Color.format + Color.reset,
        logging.ERROR: Color.fg_red + Color.format + Color.reset,
        logging.CRITICAL: Color.fg_white + Color.bg_red + Color.format + Color.reset,
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)


if __name__ == '__main__':
    log = logging.getLogger('test')
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(ColoredFormatter())
    log.addHandler(ch)

    log.info('info')
    log.debug('debug')
    log.warning('warning')
    log.error('error')
    log.critical('critical')

