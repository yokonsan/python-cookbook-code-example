from functools import wraps


class A:

    def decorate1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorate 1...')
            return func(*args, **kwargs)
        return wrapper
    
    @staticmethod
    def decorate2(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorate 2...')
            return func(*args, **kwargs)
        return wrapper


class B(A):
    """
    B继承了A，不能继承A的装饰器方法，如@B.decorate2这样使用，因为方法定义时B还没有创建
    如果需要继承，则需要实现方法：
    @A.decorate2
    def d(func):
        pass
    """
    pass

a = A()

@a.decorate1
def demo():
    pass


@A.decorate2
def demo2():
    pass


if __name__ == "__main__":
    demo()
    demo2()
