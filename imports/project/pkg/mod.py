from . import utils

def module_function():
    print("Module doing it's stuff which includes calling utils.tool")
    utils.tool()


if __name__ == '__main__':
    print(f"Invoking mod.py for {__name__}")
    module_function()
