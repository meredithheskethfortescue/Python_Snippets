import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as spatial


# todo: doc
# todo: type hints are incorrect after refactoring

def get_rectangle(width, height):
    return np.array([[0, 0],  # left bottom
                     [width, 0],  # right bottom
                     [width, height],  # right top
                     [0, height]])  # left top


def rotate(vectors: np.ndarray, alpha: float):
    theta = np.deg2rad(alpha)
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta), np.cos(theta)]])

    return [np.matmul(rotation_matrix, vector) for vector in vectors]


def translation2coordinates(shape: (float, float), translation: np.ndarray, rotation: float) -> np.ndarray:
    rect_origin = get_rectangle(*shape)
    rect_rotated = rotate(rect_origin, rotation)
    rect_translated = [point + translation for point in rect_rotated]
    return rect_translated


if __name__ == '__main__':
    np.set_printoptions(precision=3)
    fig, ax = plt.subplots()

    # shape = np.ndarray([4, 1])
    # translation = np.ndarray([4, 1])
    shape = (2, 1)
    translation = (3, 3)

    ret = translation2coordinates(shape, translation, -22.5)

    for point in get_rectangle(*shape):
        ax.scatter(*point, c='k')

    for key, point in zip(("A", "B", "C", "D"), ret):
        ax.scatter(*point, label=key)

    ax.set_aspect('equal', 'box')
    ax.legend()
    plt.show()
