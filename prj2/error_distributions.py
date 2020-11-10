import numpy as np

ERROR_DISTRIBUTIONS = {
    # Floyd & Steinberg
    'a': (1/16) * np.array(
        [[0, 0, 7],
         [3, 5, 1]]
    ),
    # Stevenson & Arce
    'b': (1/200) * np.array(
        [[ 0,  0,  0,  0,  0, 32,  0],
         [12,  0, 26,  0, 30,  0, 16],
         [ 0, 12,  0, 26,  0, 12,  0],
         [ 5,  0, 12,  0, 12,  0,  5]]
    ),
    # Burkes
    'c': (1/32) * np.array(
        [[ 0, 0, 0, 8, 4],
         [ 2, 4, 8, 4, 2]]
    ),
    # Sierra
    'd': (1/32) * np.array(
        [[0, 0, 0, 5, 3],
         [2, 4, 5, 4, 2],
         [0, 2, 3, 2, 0]]
    ),
    # Stucki
    'e': (1/42) * np.array(
        [[0, 0, 0, 8, 4],
         [2, 4, 8, 4, 2],
         [1, 2, 4, 2, 1]]
    ),
    # Jarvis, Judice, Ninke
    'f': (1/48) * np.array(
        [[0, 0, 0, 7, 5],
         [3, 5, 7, 5, 3],
         [1, 3, 5, 3, 1]]
    )
}

def get_error_distribution(edist_id):
    return ERROR_DISTRIBUTIONS[edist_id]