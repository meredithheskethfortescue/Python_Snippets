#!/usr/bin/env python3
"""Example of a generator function and its class-equivalent"""


def generator_fibonacci():
    """Generator providing the Fibonacci-Sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


class IteratorFibonacci:
    """Iterator Class providing the Fibonacci-Sequence"""

    def __init__(self):
        self.a, self.b = 0, 1

    def __next__(self):
        return_value = self.a
        self.a, self.b = self.b, self.a + self.b
        return return_value

    def __iter__(self):
        return self


def generator_loop_over_array(array):
    """Generator that loops over an array"""
    while True:
        for element in array:
            yield element


if __name__ == '__main__':
    # get an instance of the generator
    gen_fibonacci = generator_fibonacci()
    # next element can be aquired with next(...)
    for __ in range(10):
        print(next(gen_fibonacci))

    # same for the class Version...
    obj_fibonacci = IteratorFibonacci()
    for __ in range(10):
        print(next(gen_fibonacci))

    # generators are iterables
    fibonacci = generator_fibonacci()
    for idx, n in enumerate(fibonacci):
        print(n)
        if idx >= 10:
            break
