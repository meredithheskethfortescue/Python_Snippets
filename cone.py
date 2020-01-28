#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import timeit


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
