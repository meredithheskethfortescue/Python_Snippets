#!/usr/bin/env python3
"""Minimal example of a C++ to Python Binding using pybind11
Original code available at https://pybind11.readthedocs.io/en/latest/basics.html#compiling-the-test-cases
"""
import example

a, b = 1, 2
print(a, "+", b, "=", example.add(i=a, j=b))

# >>>help(example)

print("THE answer is", example.the_answer)
