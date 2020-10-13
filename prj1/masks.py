import numpy as np

MASKS = {
    'h1': [[ 0,  0, -1,  0,  0],
           [ 0, -1, -2, -1,  0],
           [-1, -2, 16, -2, -1],
           [ 0, -1, -2, -1,  0],
           [ 0,  0, -1,  0,  0]],
    'h2': (1/256) * np.array(
          [[ 1,  4,  6,  4,  1],
           [ 4, 16, 24, 16,  4],
           [ 6, 24, 36, 24,  6],
           [ 4, 16, 24, 16,  4],
           [ 1,  4,  6,  4,  1]]
    ),
    'h3': [[-1,  0,  1],
           [-2,  0,  2],
           [-1,  0,  1]],
    'h4': [[-1, -2, -1],
           [ 0,  0,  0],
           [ 1,  2,  1]],
    'h5': [[-1, -1, -1],
           [-1,  8, -1],
           [-1, -1, -1]],
    'h6': np.full(9, 1).reshape(3, 3),
    'h7': [[-1, -1,  2],
           [-1,  2, -1],
           [2, -1, -1]],
    # h8 = matrix full of -1 with main diagonal elements = 2
    'h8': np.full(9, -1).reshape(3, 3) + np.diag([3, 3, 3]),
    'h9': (1/9) * np.diag(np.full(9, 1)),
    'h10': (1/8) * np.array(
           [[-1, -1, -1, -1, -1],
            [-1,  2,  2,  2, -1],
            [-1,  2,  8,  2, -1],
            [-1,  2,  2,  2, -1],
            [-1, -1, -1, -1, -1]]
    ),
    'h11': [[-1, -1,  0],
            [-1,  0,  1],
            [ 0,  1,  1]]
}

def get_mask(mask_id):
    return np.array(MASKS[mask_id])    