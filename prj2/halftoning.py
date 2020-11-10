import cv2
import numpy as np 
from utils import halftoning
from argparser import Parser

args = Parser()
img_path = args.get_arg('image')
output_filename = args.get_arg('output_path')
error_dist = args.get_arg('error_dist')
sweep_mode = args.get_arg('sweep_mode')
skip_image_show = args.get_arg('skip_image_show')

img_path = 'images/peppers.png' if img_path is None else img_path

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
res_img = halftoning(np.array(img), edist_id=error_dist, sweep_mode=sweep_mode)

if output_filename is not None:
    cv2.imwrite(output_filename, res_img)

if not skip_image_show:
    cv2.imshow('source image', img)
    cv2.imshow('resulting image', res_img)

cv2.waitKey(0)
cv2.destroyAllWindows()