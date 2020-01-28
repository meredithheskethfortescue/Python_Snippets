#!/usr/bin/env python3

import numpy as np


def cone_complex(scope, samples):
    """Returns a simple 2D cone 
    This is necessary in many cases e.g. rotary symmetric applied 1D function on a 2D plane
    """
    '''This solution exploits the complex absolute for the euclidean distance'''
    xn = np.linspace(-scope, scope, samples)  # 1d linear progression
    xnn = xn + xn[:, np.newaxis] * 1j  # multiply with imaginary transposed
    return np.abs(xnn)  # get euclidean distance with complex absolute


def cone_mesh(scope, samples):
    """Returns a simple 2D cone 
    This is necessary in many cases e.g. rotary symmetric applied 1D function on a 2D plane
    """
    '''This naive solution builds a mesh of paired values and calculates the euclidean distance'''
    t_squared = np.linspace(-scope, scope, samples) ** 2  # squared linear progression
    mesh = np.meshgrid(t_squared, t_squared)  # build mesh of squared pairs
    return np.sqrt(np.sum(mesh, axis=0))  # get euclidean distance with the square root of the pair's sum


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    @np.vectorize
    def my_function(x):
        '''The numpy.vectorize decorator makes the function applicable to an ndarray.
        Otherwise it would throw a Value Error that The truth value of an array with more than one element is ambiguous.
        '''
        if x == 0:
            return 1
        else:
            return np.sin(x) / x


    img = my_function(cone_mesh(4*np.pi, 1001))

    v_minmax = np.amax(np.abs(img))  # scale heatmap to have zero in center
    plt.imshow(img, cmap='RdBu_r', vmin=-v_minmax, vmax=v_minmax)  # plot heatmap with white as zero
    plt.show()
