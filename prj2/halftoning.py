import cv2
import numpy as np 
from utils import halftoning
from argparser import Parser

args = Parser()
img_path = args.get_arg('image')
error_dist = args.get_arg('error_dist')

img_path = 'images/peppers.png' if img_path is None else img_path
error_dist = 'a' if error_dist is None else error_dist

img = cv2.imread(img_path, cv2.IMREAD_COLOR)
res_img = halftoning(np.array(img), edist_id=error_dist)

cv2.imshow('source image', img)
cv2.imshow('resulting image', res_img)

cv2.waitKey(0)
cv2.destroyAllWindows()