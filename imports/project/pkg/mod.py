#!/usr/bin/env python3

from . import utils  # this way `main.py` can be executed without errors
# import utils  # this way `mod.py` can be executed as __main__ without errors

def module_function():
    print(f"module_function invoked for {__name__} calls utils.tool:")
    utils.tool()


if __name__ == '__main__':
    print(f"Invoking mod.py for {__name__}")
    module_function()
