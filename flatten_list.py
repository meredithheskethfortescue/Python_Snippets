"""Flatten a 2D list"""

axes_2d = [[0, 1, 2],
           [3, 4, 5]]

axes_flat = [item for sublist in axes_2d for item in sublist]
