"""Highlight print messages"""
from contextlib import redirect_stdout
import functools
import io
from typing import Callable


def decohints(decorator: Callable) -> Callable:
    """Decorator for decorators that preserves the correct type hints in the IDE
    The type hint for a decorated function in an IDE usually gets `*args, **kwargs`.
    Since this is no helpful information, `decohints` can be used on the decorator to preserve the type hints of the
    decorated function/class.
    For original code see https://github.com/gri-gus/decohints
    """
    return decorator


@decohints
def box(_func=None, symbol: str = "="):
    """Decorator to draw a bar above and below the standard output of a function"""
    assert len(symbol) > 0, KeyError("`symbol` value must contain a character")
    assert len(symbol) == 1, NotImplementedError("Multiple symbols are not supportet yet!")

    def _decorator_box(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # catch stdout from wrapped function
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                func(*args, **kwargs)
            msg = stdout.getvalue()

            # stay quiet if stdout is empty
            if not msg:
                return

            # the longest line in output determines the length of the bars
            max_len = max([len(line) for line in msg.splitlines()])

            # print bar above stdout
            print(max_len * symbol)
            # re-redirect message to stdout but strip trailing whitespace in order to
            # place the trailing bar tight below the message
            print(msg.rstrip())
            # print bar below stdout
            print(max_len * symbol + "\n")

        return wrapper

    if _func is None:
        return _decorator_box
    else:
        return _decorator_box(_func)


if __name__ == '__main__':
    @box
    def verbose_function(world: str = "world"):
        """Print some stuff to stdout"""
        print(f"Hello, {world}!")
        print()
        print("Lorem ipsum, dolor sit.")
        print("Amet consectetuer, adipiscing")
        print("elitr ut purus invidunt.")


    @box(symbol="+")
    def bark():
        print("Bleh!")


    @box
    def silent_function():
        pass


    # bar adapts to the max line length - in these cases the body.
    verbose_function("Eros")
    verbose_function("Io")
    # a very long name will cause the bar length to be extended in order to fit the content
    verbose_function("XavlegbmaofffassssitimiwoamndutroabcwapwaelippohfffX")
    verbose_function("Phoebe")

    # this one has a different symbol
    bark()

    # a function call that does not print to stdout stays silent despite being decorated
    silent_function()

    # let's see if the help function still get's the correct docstring
    help(verbose_function)
