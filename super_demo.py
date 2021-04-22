class Base:
    def __init__(self):
        print('Enter Base.')
        print('Leave Base.')


class A(Base):
    def __init__(self):
        print('Enter A.')
        super(A, self).__init__()
        print('Leave A.')


class B(Base):
    def __init__(self):
        print('Enter B.')
        super().__init__()
        print('Leave B.')


class C(A, B):
    def __init__(self):
        print('Enter C.')
        super().__init__()
        print('Leave C.')


if __name__ == "__main__":
    # a = A()
    # b = B()
    c = C()
    print(C.mro())
