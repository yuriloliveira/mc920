import numpy as np
import cv2
import math
from matplotlib import pyplot as plt
from error_distributions import get_error_distribution

def halftoning(img, edist_id='a', sweep_mode='default'):
    PIXEL_SIZE = 3 # only supports rgb images
    (height, width, _) = img.shape
    result = np.zeros((height, width, PIXEL_SIZE))
    error_distribution = get_error_distribution(edist_id)
    
    for row in range(0, height):
        row_range_min = 0 if sweep_mode != 'alternate' or row % 2 == 0 else width -1
        row_range_max = width if row_range_min == 0 else -1
        # IMPORTANTE: Comentar no relatório necessidade de utilizar step para alternado funcionar
        step = 1 if row_range_min == 0 else -1
        for col in range(row_range_min, row_range_max, step):
            result[row][col] = convert_pixel(img[row][col])
            err_rgb = get_error_rgb(img[row][col], result[row][col]) 
            apply_err(img, (row, col), err_rgb, error_distribution)

    #####################################################################
    ### IMPORTANTE: Comparar sem normalize/com normalize no relatório ###
    ### return result                                                 ###
    #####################################################################
    return cv2.normalize(
        result,
        None,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_32F
    ).astype(np.uint8)

def convert_pixel(curr_pixel):
    [b, g, r] = curr_pixel
    return [
        0 if b < 128 else 1,
        0 if g < 128 else 1,
        0 if r < 128 else 1
    ]

def get_error_rgb(old_pi, new_pi, pi_length=3):
    result = np.zeros((3))
    for i in range(0, pi_length):
        # IMPORTANTE: Comparar com indexização errada no pixel no relatório
        # result[i] = old_pi[0] - new_pi[0] * 255
        result[i] = old_pi[i] - new_pi[i] * 255
    return result

def apply_err(img, pi_pos, error_rgb, edist):
    (w, h) = edist.shape
    (x, y) = pi_pos
    half_w = math.floor(w / 2)

    for i in range(0, w):
        for j in range(0, h):
            target_x = x + i - half_w # Abordar esta decisão no relatório (limitação)
            target_y = y + j
            if target_x < 0 or target_y < 0 or\
               target_x >= img.shape[0] or target_y >= img.shape[1]:
               continue
            for band in range(0, 3):
                img[target_x][target_y][band] =\
                    img[target_x][target_y][band] +\
                    edist[i][j] * error_rgb[band]

def plot_histogram(img):
    bands = ['b', 'g', 'r']
    for i in range(0, 3):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, 'o', color=bands[i], label=bands[i])
    plt.show()