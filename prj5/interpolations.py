import numpy as np
import cv2

def closest_neighboor(img, scale_factor=1):
    img_h, img_w = img.shape
    res_h = round(img_h * scale_factor)
    res_w = round(img_w * scale_factor)
    res = np.zeros((res_w * res_h, 1))
    # [0, 0, ... 0, res_w, ..., res_w] / scale_factor
    x_indexes = np.round(np.floor(np.arange(res_w * res_w) / res_w) / scale_factor).astype(np.uint32)
    # [0, 1, 2, ..., img_h, ..., 0, 1, 2, ..., img_h] / scale_factor
    y_indexes = np.round(np.resize(np.arange(res_h), res_h * res_h) / scale_factor).astype(np.uint32)
    x_indexes[x_indexes >= img_w] = img_w - 1
    y_indexes[y_indexes >= img_h] = img_h - 1
    res = img[x_indexes, y_indexes]
    return __normalize(res.reshape(res_h, res_w), 0, 255)

def __normalize(img, min, max):
    return cv2.normalize(
        img,
        None,
        alpha=min,
        beta=max,
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_32F
    ).astype(np.uint8)