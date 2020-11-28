import cv2
import numpy as np

from argparser import Parser
from thresholding_method import ThresholdingMethod

args = Parser()
# Command arguments
img_path = args.get_arg('image')
method = args.get_arg('method')

img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
thres_method = ThresholdingMethod(method)
res_img = thres_method.process(img)

cv2.imshow('source image', img)
cv2.imshow('resulting image', res_img)
cv2.waitKey()