import numpy as np
from scipy.ndimage import generic_filter
import math

def thres_global(img, threshold=128):
    return generic_filter(img, lambda pi: 0 if pi > threshold else 255, size=(1,1))

def thres_bernsen(img, n=3):
    threshold_matrix = generic_filter(img, bernsen_aux, footprint=build_footprint(n))
    return apply_threshold(img, threshold_matrix)

def bernsen_aux(ng):
    return (np.min(ng) + np.max(ng)) / 2

def apply_threshold(img, threshold_matrix):
    res_img = np.zeros(img.shape)
    res_img[img <= threshold_matrix] = 255
    return res_img

def build_footprint(n):
    footprint = np.ones((n,n))
    mid = math.floor(n/2)
    footprint[mid][mid] = 0
    return footprint