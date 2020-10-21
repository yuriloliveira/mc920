import cv2
import numpy as np
import sys
from argparse import ArgumentParser
from masks import get_mask
from filter_utils import show_filtered_image, filter_image, add_filters, show_src_and_filtered_image

MASK_COUNT = 11

parser = ArgumentParser('Applies mask to image')
parser.add_argument('--image', '-i', help='path to image which will be filtered', dest='image')
parser.add_argument('--mask', '-m', help='mask to be applied to the image. Available masks are h1..h11', default='h1', dest='mask')
parser.add_argument('--out', '-o', help='path to output of filtering (output will be an .png image)', dest='output_path')
parser.add_argument('--outc', '-oc', help='path to output of combined images', dest='output_combined_path')
parser.add_argument('--hflip', '-hf', help='if passed, flips the resulting image horizontally', dest='hflip', action='store_true')
args = vars(parser.parse_args())

filename = args['image']
mask_id = args['mask']
output_filename = args['output_path']
output_combined_filename = args['output_combined_path']
hflip = args['hflip']

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
flip_axis = 1 if hflip else None
print(flip_axis)
(filtered_image, combined_filters_image) = show_filtered_image(img, mask_id, flip_axis=flip_axis)

if (output_filename):
    cv2.imwrite(output_filename, filtered_image)
    if (combined_filters_image is not None and output_combined_filename):
        cv2.imwrite(output_combined_filename, combined_filters_image)

cv2.waitKey(0)
cv2.destroyAllWindows()