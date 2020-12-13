import cv2
import numpy as np
from matplotlib import pyplot as plt
from argparser import Parser
from codify import codify

args = Parser()
# Command arguments
mode = args.get_arg('mode')
imgin_path = args.get_arg('imagein')
imgout_path = args.get_arg('imageout')
textin_path = args.get_arg('textin')
textout_path = args.get_arg('textout')

img = cv2.imread(imgin_path, cv2.IMREAD_COLOR)
if mode == 'codify':
    res_img = codify(img, '')
    cv2.imwrite(imgout_path, res_img)