import cv2
import numpy as np
import sys
from argparse import ArgumentParser
from masks import get_mask
from filter_utils import show_filtered_image

MASK_COUNT = 11

parser = ArgumentParser('Applies mask to image', allow_abbrev=True)
parser.add_argument('--image', '-i', help='image to be filtered', dest='image')
parser.add_argument('--masks', '-m', help='mask(s) to be applied to the image. Available masks are h1..h11', nargs='+', default='h1', dest='masks')
args = vars(parser.parse_args())

filename = args['image']
mask_ids = args['masks']

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

for mask_id in mask_ids:
    try:
        show_filtered_image(img, mask_id)
    except Exception as e:
        print("An error occurred: ", e)

cv2.waitKey(0)
cv2.destroyAllWindows()