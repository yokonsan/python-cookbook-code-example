from functools import wraps
import time

def timethis(func):
    """函数执行时间"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('函数：{0}，执行时间：{1}'.format(func.__name__, end-start))
        return result
    
    return wrapper


@timethis
def demo(n):
    print(f'n: {n}')
    while n > 0:
        n -= 1


if __name__ == "__main__":
    demo(10000)
    demo.__wrapped__(1000)
