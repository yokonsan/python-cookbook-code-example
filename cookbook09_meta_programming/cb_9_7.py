from inspect import signature
from functools import wraps


def type_assert(*args, **kwargs):
    """
    函数参数类型校验
    瑕疵：函数带默认值的参数无法被校验，sig.bind()无法获取到默认值参数
    """
    def decorate(func):
        if not __debug__:
            return func
        sig = signature(func)
        bound_types = sig.bind_partial(*args, **kwargs).arguments
        print(f'bound_types: {bound_types}')

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            print(f'bound_values: {bound_values}')
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))

            return func(*args, **kwargs)
        return wrapper
    return decorate


@type_assert(int, y=int, z=int)
def add(x, y, z='4'):
    print(x + y + z)


if __name__ == "__main__":
    # def demo(x, y, z=4):
    #     return x + y + z
    
    # sig = signature(demo)
    # print(sig)
    # print(sig.parameters)
    # print(sig.parameters['z'])
    # print(sig.parameters['z'].default)
    # print(sig.parameters['z'].name)
    # print(sig.parameters['z'].kind)
    # bound_types = sig.bind_partial(int,z=int)
    # print(bound_types)
    # print(dir(bound_types))
    # print(bound_types.arguments)

    # bound_values = sig.bind(1, 2)
    # print(bound_values)

    add(1, 3)
