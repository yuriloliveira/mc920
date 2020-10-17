import cv2
import numpy as np
import sys
from argparse import ArgumentParser
from masks import get_mask
from filter_utils import show_filtered_image, filter_image, add_filters, show_src_and_filtered_image

MASK_COUNT = 11

parser = ArgumentParser('Applies mask to image', allow_abbrev=True)
parser.add_argument('--image', '-i', help='image to be filtered', dest='image')
parser.add_argument('--mask', '-m', help='mask to be applied to the image. Available masks are h1..h11', default='h1', dest='mask')
args = vars(parser.parse_args())

filename = args['image']
mask_id = args['mask']

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
show_filtered_image(img, mask_id)

cv2.waitKey(0)
cv2.destroyAllWindows()