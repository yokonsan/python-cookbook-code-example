from functools import wraps
import logging


def logger(level, name=None, message=None):

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    
    return decorate

# @logger(logging.ERROR, name='DEMO', message='demo...')
def demo(x, y):
    print(x + y)


# @logger(logging.CRITICAL)
def spam():
    print('Spam!')


if __name__ == "__main__":
    # print(demo(3, 4))
    logger(logging.DEBUG)(demo)(3, 4)
