import cv2
import numpy as np
from matplotlib import pyplot as plt

from argparser import Parser
from codify import codify
from decodify import decodify
from bitplane_utils import extract_rgb_bitplane, merge_rgb

args = Parser()
# Command arguments
mode = args.get_arg('mode')
imgin_path = args.get_arg('imagein')
imgout_path = args.get_arg('imageout')
textin_path = args.get_arg('textin')
textout_path = args.get_arg('textout')
bitplan = args.get_arg('bitplan')

img = cv2.imread(imgin_path, cv2.IMREAD_COLOR)
if mode == 'codify':
    res_img = codify(img, open(textin_path).read(), bitplan=bitplan)
    cv2.imwrite(imgout_path, res_img)
elif mode == 'decodify':
    decodified_msg = decodify(img, bitplan=bitplan)
    textout_file = open(textout_path, 'w')
    textout_file.write(str(decodified_msg))
    textout_file.close()
elif mode == 'bitplanes':
    for bitplane in [0, 1, 2, 7]:
        bitplane_blue, bitplane_green, bitplane_red = extract_rgb_bitplane(img, bitplane)
        bitplanes_img = merge_rgb(bitplane_blue, bitplane_green, bitplane_red)
        cv2.imshow('bitplane ' + str(bitplane), bitplanes_img)
    cv2.waitKey()
    cv2.destroyAllWindows()