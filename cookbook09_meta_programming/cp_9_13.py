# 使用元类，控制类实例化时操作
class NoInstance(type):
    """使得继承该元类的类不能被实例化"""
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Example
class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print(f'Spam.grok x:{x}')


# 单例模式
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        
        return self.__instance


# Example
class Spam2(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam2')


# cache
class Cache(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = {}
    
    def __new__(cls, name, bases, attrs):
        pass
    
    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        
        obj = super().__call__(*args)
        self.__cache[args] = obj
        return obj


# Example
class Spam3(metaclass=Cache):
    def __init__(self, name):
        print('Creating Spam3({!r})'.format(name))
        self.name = name


if __name__ == "__main__":
    # ex1
    # Spam.grok(11)
    # s = Spam()
    # s.grok(111)

    # ex2
    # s1 = Spam2()
    # s2 = Spam2()
    # print(s1 is s2)

    # ex3
    a = Spam3('A')
    b = Spam3('B')
    c = Spam3('A')
    print(a is b)
    print(a is c)
    print()
