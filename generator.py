#!/usr/bin/env python3


class IteratorClass:
    """Iterator Class"""

    def __init__(self):
        self.a, self.b = 0, 1

    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a + self.b
        return return_value

    def __iter__(self):
        return self


def generator_function():
    """Generator providing the Fibonacci-Sequence
    get the next element with next()
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # get instance of the generator
    gen_fibonacci = generator_function()
    # next element can be aquired with next(...)
    for __ in range(10):
        print(next(gen_fibonacci))

    # same for the class Version...
    obj_fibonacci = IteratorClass()
    for __ in range(10):
        print(next(gen_fibonacci))

    # generators are iterables
    fibonacci = generator_function()
    for idx, n in enumerate(fibonacci):
        print(n)
        if idx >= 10:
            break
