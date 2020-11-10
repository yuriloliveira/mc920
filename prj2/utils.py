import numpy as np
import math
from error_distributions import get_error_distribution


def halftoning(img, edist_id='a'):
    PIXEL_SIZE = 3 # only supports rgb images
    (width, height, _) = img.shape
    result = np.zeros((width, height, PIXEL_SIZE))
    error_distribution = get_error_distribution(edist_id)

    for x in range(0, width):
        for y in range(0, height):
            result[x][y] = convert_pixel(img[x][y])
            err_rgb = get_error_rgb(img[x][y], result[x][y]) 
            apply_err(img, (x, y), err_rgb, error_distribution)

    return result

def convert_pixel(curr_pixel):
    [r, g, b] = curr_pixel
    return [
        0 if r < 128 else 1,
        0 if g < 128 else 1,
        0 if b < 128 else 1
    ]

def get_error_rgb(old_pi, new_pi, pi_length=3):
    result = np.zeros((3))
    for i in range(0, pi_length):
        result[i] = old_pi[0] - new_pi[0] * 255
    return result

def apply_err(img, pi_pos, error_rgb, edist):
    (w, h) = edist.shape
    (x, y) = pi_pos
    half_w = math.floor(w / 2)

    for i in range(0, w):
        for j in range(0, h):
            target_x = x + i - half_w
            target_y = y + j
            if target_x < 0 or target_y < 0 or\
               target_x >= img.shape[0] or target_y >= img.shape[1]:
               continue
            for band in range(0, 3):
                img[target_x][target_y][band] =\
                    img[target_x][target_y][band] +\
                    edist[i][j] * error_rgb[band]