from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.ERROR, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper

# Example use
@logged  # logged实际上是一个函数，不带括号，相当于 logged(add)，partial偏函数处理后相当于 looged(level=logging.ERROR, name=None, message=None)(add)
def add(x, y):
    print(x + y)
    return x + y

@logged(level=logging.CRITICAL, name='example')  # 相当于 looged(level=logging.CRITICAL, name='example')(spam)
def spam():
    print('Spam!')


if __name__ == "__main__":
    add(2, 3)
    spam()
