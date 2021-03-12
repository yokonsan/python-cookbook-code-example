import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)  # 被包装函数的元信息复制到可调用实例中去。
        self.ncalls = 0
    
    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        return types.MethodType(self, instance)


def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    
    wrapper.ncalls = lambda: ncalls  # 相当于9.5中设置函数
    return wrapper


@Profiled
def add(x, y):
    print(x + y)


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


@profiled
def add2(x, y):
    print(x + y)


if __name__ == "__main__":
    add(1, 2)
    s = Spam()
    s.bar(3)
    print(s.bar.ncalls)

    add2(2, 3)
    add2(4, 5)
    print(add2.ncalls())
