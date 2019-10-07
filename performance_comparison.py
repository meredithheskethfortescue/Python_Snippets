#!/usr/bin/env python3
"""Performance measurement
Example of comparing the calculation speed of two instructions that produce an identical output.
By using the `out` parameter in numpy a speedup can be achieved because no new array needs to be created.
"""


import timeit
import numpy as np

init = """
import numpy as np
arr = np.random.rand(2, 3000, 4000).astype(np.float32)
"""

f1="""
np.log(arr, out=a)
"""

f2="""
arr = np.log(arr)
"""

loops = 100
print(timeit.timeit(stmt=f1, setup=init, number=loops) / loops)
print(timeit.timeit(stmt=f2, setup=init, number=loops) / loops)
