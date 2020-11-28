import numpy as np
from scipy.ndimage import generic_filter
import math

DEFAULT_N = 3

def thres_global(img, threshold=128):
    return generic_filter(img, lambda pi: 0 if pi > threshold else 255, size=(1,1))

def thres_bernsen(img, n=DEFAULT_N):
    threshold_matrix = generic_filter(img, bernsen_aux, size=(n,n))
    return apply_threshold(img, threshold_matrix)

def thres_niblack(img, n=DEFAULT_N, k=0.1):
    threshold_matrix = generic_filter(img, niblack_aux(k), size=(n,n))
    return apply_threshold(img, threshold_matrix)

def thres_sauvola_pietaksinen(img, n=DEFAULT_N, k=0.5, R=4):
    threshold_matrix = generic_filter(img, sauvola_aux(k, R), size=(n,n))
    return apply_threshold(img, threshold_matrix)

def thres_phansalskar(img, n=DEFAULT_N, k=0.25, R=0.5, p=2, q=10):
    threshold_matrix = generic_filter(img, phansalskar_aux(k, R, p, q), size=(n,n))
    return apply_threshold(img, threshold_matrix)

def thres_contrast(img, n=DEFAULT_N):
    threshold_matrix = generic_filter(img, contrast_aux, size=(n,n))
    return apply_threshold(img, threshold_matrix)

def thres_mean(img, n=DEFAULT_N):
    threshold_matrix = generic_filter(img, np.mean, size=(n,n))
    return apply_threshold(img, threshold_matrix)

def thres_median(img, n=DEFAULT_N):
    threshold_matrix = generic_filter(img, np.median, size=(n,n))
    return apply_threshold(img, threshold_matrix)

def bernsen_aux(ng):
    return (np.min(ng) + np.max(ng)) / 2

def niblack_aux(k):
    def aux(ng):
        return np.mean(ng) + (k * np.std(ng))
    return aux

def sauvola_aux(k, R):
    def aux(ng):
        return np.mean(ng) * (1 + (k * ((np.std(ng) / R) - 1)))
    return aux

def phansalskar_aux(k, R, p, q):
    def aux(ng):
        mean = np.mean(ng)
        return mean * (1 + p * math.exp(-q * mean) + k * ((np.std(ng) / R) - 1))
    return aux

def contrast_aux(ng):
    curr_pi = ng[math.floor(ng.shape[0] / 2)]
    closer_to_max = abs((curr_pi - np.min(ng))) - abs((curr_pi - np.max(ng)))
    return 255 if closer_to_max else 0

def apply_threshold(img, threshold_matrix):
    res_img = np.zeros(img.shape)
    res_img[img <= threshold_matrix] = 255
    return res_img