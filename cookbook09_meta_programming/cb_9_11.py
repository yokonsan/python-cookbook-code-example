from functools import wraps
import inspect


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print(f'Debuging: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper


@optional_debug
def add(x, y):
    print(x + y)

@optional_debug
def add2(x, y):
    print(x + y)


if __name__ == "__main__":
    add(1, 2, debug=True)
    add2(3, 4)
