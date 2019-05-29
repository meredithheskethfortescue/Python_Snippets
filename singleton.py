#!/usr/bin/env python3


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class IteratorClass(metaclass=Singleton):
    def __init__(self):
        self.a, self.b = 0, 1

    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a + self.b
        return return_value

    def __iter__(self):
        return self


if __name__ == '__main__':
    for __ in range(10):
        print(next(IteratorClass()))
