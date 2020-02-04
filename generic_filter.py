#!/usr/bin/env python3

import numpy as np
from scipy import ndimage


def my_filter_wrapper(img: np.ndarray, kernel_width: int, nop: int = 0) -> np.ndarray:
    """Box blur that ignores areas that are marked as No Operation (NOP)"""

    assert img.ndim == 2, "Input data is not 2D."
    assert kernel_width % 2, "kernel_width must be odd."

    img = np.array(img, dtype=np.float32)

    def kernel_function(subset):
        """Kernel function that is applied to each pixel"""
        centerpoint = subset[np.size(subset) // 2]  # get central pixel of the windowed subset
        if centerpoint == nop:
            # current pixel marked as NOP
            return 0
        else:
            # box blur
            return np.mean(subset[subset != nop])

    # call filter
    return ndimage.generic_filter(img,
                                  lambda subset: kernel_function(subset),
                                  kernel_width,
                                  cval=0,
                                  mode='constant')
