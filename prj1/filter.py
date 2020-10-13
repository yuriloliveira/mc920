import numpy as np

def filter_pixel(img, pixel, mask):
    x = pixel[0]
    y = pixel[1]
    offset_size = int(np.floor(mask.shape[0] / 2))
    target_slice = img[x-offset_size:x+offset_size+1, y-offset_size:y+offset_size + 1]
    return np.uint8(np.round(np.sum(target_slice* mask) / np.sum(mask)))

def apply_filter(img, mask):
    mask_offset = int(np.floor(mask.shape[0] / 2))
    result = np.zeros(img.shape, dtype=np.uint8)
    for x in range(mask_offset, img.shape[0] - mask_offset):
        for y in range(mask_offset, img.shape[1] - mask_offset):
            result[x][y] = filter_pixel(img, (x, y), mask)
    return result