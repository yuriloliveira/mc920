import cv2
import numpy as np

from argparser import Parser
from thresholding_method import ThresholdingMethod,  ThresholdingConfig

args = Parser()
# Command arguments
img_path = args.get_arg('image')
method = args.get_arg('method')
T = args.get_arg('T')
n = args.get_arg('n')
k = args.get_arg('k')
R = args.get_arg('R')
p = args.get_arg('p')
q = args.get_arg('q')

img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
thres_method = ThresholdingMethod(method)
res_img = thres_method.exec(img, ThresholdingConfig(T=T, n=n, k=k, R=R, p=p, q=q))

cv2.imshow('source image', img)
cv2.imshow('resulting image', res_img)
cv2.waitKey()