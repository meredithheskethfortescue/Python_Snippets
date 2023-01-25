"""Highlight print messages"""
from contextlib import redirect_stdout
import functools
import io


def box(func):
    """Decorator to draw a bar above and below the standard output of a function"""

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
        print(max_len * "=")
        # re-redirect message to stdout but strip trailing whitespace in order to
        # place the trailing bar tight below the message
        print(msg.rstrip())
        # print bar below stdout
        print(max_len * "=" + "\n")

    return wrapper


if __name__ == '__main__':
    @box
    def verbose_function(world: str = "world"):
        print(f"Hello, {world}!")
        print()
        print("Lorem ipsum, dolor sit.")
        print("Amet consectetuer, adipiscing")
        print("elitr ut purus invidunt.")


    @box
    def silent_function():
        pass


    # bar adapts to the max line length - in these cases the body.
    verbose_function("Eros")
    verbose_function("Io")
    # a very long name will cause the bar length to be extended in order to fit the content
    verbose_function("XavlegbmaofffassssitimiwoamndutroabcwapwaelippohfffX")
    verbose_function("Phoebe")

    # a function call that does not print to stdout stays silent despite being decorated
    silent_function()
