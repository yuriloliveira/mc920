import cv2
import numpy as np
from matplotlib import pyplot as plt
from argparser import Parser
from thresholding_method import ThresholdingMethod,  ThresholdingConfig

args = Parser()
# Command arguments
img_path = args.get_arg('image')
out_path = args.get_arg('out')
method = args.get_arg('method')
T = args.get_arg('T')
n = args.get_arg('n')
k = args.get_arg('k')
R = args.get_arg('R')
p = args.get_arg('p')
q = args.get_arg('q')
display_mode = args.get_arg('display_mode')

img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
thres_method = ThresholdingMethod(method)
res_img = thres_method.exec(img, ThresholdingConfig(T=T, n=n, k=k, R=R, p=p, q=q))

if (out_path):
        cv2.imwrite(out_path, res_img)

if display_mode == 'hist':
    (h, w) = res_img.shape
    print(np.count_nonzero(res_img == 0) / (h * w))
    plt.hist(img.ravel(), 256, [0,256])
    plt.show()
elif display_mode == 'off':
    quit()
else:
    cv2.imshow('source image', img)
    cv2.imshow('resulting image', res_img)
    cv2.waitKey()