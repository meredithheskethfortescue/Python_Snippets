"""Highlight print messages"""
import io
from contextlib import redirect_stdout


def emphasize_stdout(func):
    """Decorator to draw a line above and below the standard output of a function"""

    def wrapper(*args, **kwargs):
        # catch stdout from wrapped function
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            func(*args, **kwargs)
        msg = stdout.getvalue()

        # stay quiet if stdout is empty
        if not msg:
            return

        # the longest line in output determines the length of the lines
        max_len = max([len(line) for line in msg.splitlines()])

        # print line above stdout
        print(max_len * "=")
        # re-redirect message to stdout but strip trailing whitespace in order to
        # place the trailing line tight below the message
        print(msg.rstrip())
        # print line below stdout
        print(max_len * "=")

    return wrapper


@emphasize_stdout
def verbose_function(world: str = "world"):
    print(f"Hello, {world}!")
    print()
    print("Lorem ipsum, dolor sit.")
    print("Amet consectetuer, adipiscing elitr ut purus invidunt.")


if __name__ == '__main__':
    verbose_function("Alpha Centauri")
