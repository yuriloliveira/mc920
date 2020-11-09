import cv2
import numpy as np 
from utils import floyd_stein
from argparser import Parser

args = Parser()
img_path = args.get_arg('image')
img_path = 'images/peppers.png' if img_path is None else img_path
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
res_img = floyd_stein(np.array(img))
cv2.imshow('source image', img)
cv2.imshow('resulting image', res_img)

cv2.waitKey(0)
cv2.destroyAllWindows()