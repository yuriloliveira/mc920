import numpy as np
import cv2

def filter_pixel(img, pixel, mask):
    x = pixel[0]
    y = pixel[1]
    offset_size = int(np.floor(mask.shape[0] / 2))
    target_slice = img[x-offset_size:x+offset_size+1, y-offset_size:y+offset_size + 1]
    return np.uint8(np.round(np.sum(target_slice* mask) / np.sum(mask)))

def apply_filter(img, mask):
    # non-vectorized form, assuming mask of 3x3
    # places zero into border pixels
    result = np.zeros(img.shape, dtype=np.uint8)
    for x in range(1, img.shape[0] - 1):
        for y in range(1, img.shape[1] - 1):
            result[x][y] = filter_pixel(img, (x, y), mask)
    return result

img = cv2.imread('./images/lena.png', cv2.IMREAD_GRAYSCALE)

h6 = (1/9) * np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
filtered_image = apply_filter(img, h6)
print(filtered_image.shape)
cv2.imshow('image', img)
cv2.imshow('filtered image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()