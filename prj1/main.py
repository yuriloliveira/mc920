import cv2
import sys
from masks import get_mask
from filter import apply_filter

filename = sys.argv[1] if len(sys.argv) == 2 else './images/lena.png'
mask_id = sys.argv[2] if len(sys.argv) == 3 else 'h1'

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
mask = get_mask(mask_id)
filtered_image = apply_filter(img, mask)

cv2.imshow('image', img)
cv2.imshow('filtered image (mask=' + mask_id + ')', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()