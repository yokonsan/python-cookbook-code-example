from functools import partial, wraps
import logging

from cb_9_3 import timethis


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logger(level, name=None, message=None):

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        
        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level
        
        @attach_wrapper(wrapper)
        def set_message(new_msg):
            nonlocal logmsg
            logmsg = new_msg

        return wrapper
    
    return decorate


@timethis
@logger(logging.ERROR)
def add(x, y):
    print(x + y)
    return x + y


@logger(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    add(2, 3)
    add.set_level(logging.CRITICAL)
    add(3, 4)
    add.set_message('err')
    add(4, 5)

