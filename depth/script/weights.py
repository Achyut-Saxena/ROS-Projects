"""
File to edit to get set of directional weights
"""

import math


def get_sin_weights():
    """
    Returns array of sine weights
    """

    weight_array = []
    for angle in range(0, 181):
        weight_array.append(math.sin(math.radians(angle)))

    return weight_array


def get_cos_weights():
    """
    Returns array of cosine weights
    """

    weight_array = []
    for angle in range(0, 181):
        weight_array.append(math.cos(math.radians(angle)))

    return weight_array
