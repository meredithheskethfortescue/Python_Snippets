#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # see plot_wireframe

plt.rcParams['text.usetex'] = True  # LaTeX rendering support


def plot_quiver(img):
    __, height, width = np.shape(img)
    x = list(range(width))
    y = list(reversed(range(height)))
    # y = list(range(height))

    fig, ax = plt.subplots()
    ax.quiver(x, y, img[1], -img[0])
    plt.show()


def plot_wireframe(two_dim_array, show=True):
    """Setup a 2d array as 3d-plot and show window.
    :param two_dim_array: 2d array of data to be plotted
    :param show: If True open up window directly
    :return: Matplotlib surface plot
    """
    # Keep in mind the need of additional import:
    # from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ny, nx = two_dim_array.shape
    x = np.linspace(0, 1, nx)
    y = np.linspace(0, 1, ny)
    xv, yv = np.meshgrid(x, y)
    surf = ax.plot_surface(xv, yv, two_dim_array, cmap='nipy_spectral')
    if show:
        plt.show()
    return surf


def plot_polar(r, phi):
    fig = plt.figure(tight_layout=True)
    ax = fig.add_subplot(111, projection='polar')
    ax.plot(phi, r)
    ax.grid(label='size')
    plt.show()


def multiple_images_one_colorbar():
    w = 8
    img_a = np.random.uniform(0, 1, (w, w))
    img_b = np.random.uniform(0, .25, (w, w))
    img_c = np.random.uniform(0, 2, (w, w))
    img_d = np.random.uniform(.3, .7, (w, w))


    def minmax(*arr: np.ndarray) -> (float, float):
        """Collect min and max from several arrays. Minimal range is limited to 0..1."""
        return np.amin([a.min() for a in arr] + [0.]), np.max([a.max() for a in arr] + [1.])


    vmin, vmax = minmax(img_a, img_b, img_c)
    print(vmin, vmax)

    fig, axes = plt.subplots(2, 2)
    for ax, img in zip(axes.flat, [img_a, img_b, img_c, img_d]):
        # ax.set_axis_off()
        img_handle = ax.imshow(img, cmap='gray', vmin=vmin, vmax=vmax)

    cbar = fig.colorbar(img_handle, ax=axes.ravel().tolist())

    plt.show()


def cone(scope, samples):
    t_squared = np.linspace(-scope, scope, samples) ** 2
    line_2d = np.empty((samples, samples))
    line_2d[:] = t_squared
    return np.sqrt(line_2d + np.transpose(line_2d))


def morlet(t, f):
    s = 7 / (2 * np.pi * f)
    return np.cos(2 * np.pi * f * t) * np.exp(- t ** 2 / (2 * s ** 2))


def maximize_window():
    """Maximize a matplotlib plot window when shown"""
    backend = plt.get_backend()
    figure_manager = plt.get_current_fig_manager()

    if backend == 'TkAgg':
        import platform
        operating_system = platform.system()

        if operating_system in ('Linux', 'Darwin'):  # Darwin is for Mac
            figure_manager.resize(*figure_manager.window.maxsize())
        elif operating_system == 'Windows':
            figure_manager.window.state('zoomed')
        else:
            import warnings
            warnings.warn("Unknown operating system:" + str(operating_system))

    elif backend == 'wxAgg':
        figure_manager.frame.Maximize(True)

    elif backend in ('Qt4Agg', 'Qt5Agg'):
        figure_manager.window.showMaximized()

    else:
        import warnings
        msg = "No window maximizing routine found for backend '" + backend + "' found."
        warnings.warn(msg)


if __name__ == '__main__':
    # create data
    scope = np.pi
    samples = 31
    wavelet_1d = np.cos(np.linspace(-scope, scope, samples))
    cone = cone(scope, samples)
    wavelet_2d = np.cos(cone)  # cos(r) if -pi <= r <= pi
    wavelet_2d[cone > np.pi] = -1  # -1 else

    # line plot
    plt.plot(wavelet_1d)
    plt.show()

    # image plot
    plt.imshow(wavelet_2d, cmap='nipy_spectral')
    plt.show()

    # plot as 3D wireframe
    plot_wireframe(wavelet_2d)

    # quiver plot of a vectorfield
    grad = np.gradient(wavelet_2d)
    print(grad)
    plot_quiver(grad)

    # Lambert in polar coordinate system
    xn = np.linspace(0, 2 * np.pi, 360)
    yn = np.cos(xn) / 2 + 0.5
    plot_polar(yn, xn)

    
