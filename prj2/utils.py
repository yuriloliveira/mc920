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
    (edist_w, edist_h, _) = error_distribution.shape

    for row in range(0+edist_h, height-edist_h):
        row_range_min = 0 if sweep_mode != 'alternate' or row % 2 == 0 else width -1
        row_range_max = width if row_range_min == 0 else -1
        step = 1 if row_range_min == 0 else -1
        for col in range(row_range_min+edist_w, row_range_max-edist_w, step):
            result[row][col] = convert_pixel(img[row][col])
            err_rgb = get_error_rgb(img[row][col], result[row][col]) 
            apply_err(img, (row, col), err_rgb, error_distribution)

    return cv2.normalize(
        result,
        None,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_32F
    ).astype(np.uint8)

def convert_pixel(curr_pixel):
    pixel = np.array(curr_pixel)
    pixel[curr_pixel < 128] = 0
    pixel[curr_pixel >= 128] = 1
    return pixel

def get_error_rgb(old_pi, new_pi, pi_length=3):
    result = np.zeros((3))
    return old_pi - (new_pi * 255)

def apply_err(img, pi_pos, error_rgb, edist):
    (w, h, _) = edist.shape
    (x, y) = pi_pos
    half_w = math.floor(w / 2)
    img[x - half_w:x + half_w+1, y:y+h] = img[x - half_w:x + half_w+1,y:y+h] + (edist * error_rgb)

def plot_histogram(img):
    bands = ['b', 'g', 'r']
    for i in range(0, 3):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, 'o', color=bands[i], label=bands[i])
    plt.show()