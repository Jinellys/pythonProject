import logging

try:
    raise ZeroDivisionError("OOOOOPS!!!")
    # division = 5 / 0
except ZeroDivisionError:
    print('На ноль делить нельзя')
    logging.error('ZeroDivisionError')
finally:
    print('exit')
