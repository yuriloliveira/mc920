import cv2
import numpy as np
import sys
# from argparse import ArgumentParser
from argparser import Parser
from masks import get_mask
from filter_utils import show_filtered_image, filter_image, add_filters, show_src_and_filtered_image

MASK_COUNT = 11

parser = Parser()
filename = parser.get_arg('image')
mask_id = parser.get_arg('mask')
output_filename = parser.get_arg('output_path')
output_combined_filename = parser.get_arg('output_combined_path')
hflip = parser.get_arg('hflip')

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
flip_axis = 1 if hflip else None
(filtered_image, combined_filters_image) = show_filtered_image(img, mask_id, flip_axis=flip_axis)

if (output_filename):
    cv2.imwrite(output_filename, filtered_image)
    if (combined_filters_image is not None and output_combined_filename):
        cv2.imwrite(output_combined_filename, combined_filters_image)

cv2.waitKey(0)
cv2.destroyAllWindows()