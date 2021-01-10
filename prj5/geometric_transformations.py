import cv2
from argparser import Parser
from interpolations import closest_neighboor

args = Parser()
mode = args.get_arg('mode')
input_path = args.get_arg('input-image')
output_path = args.get_arg('output-image')
angle = args.get_arg('angle')
scale_factor = args.get_arg('scale-factor')
dimension = args.get_arg('image-dimension')

img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
interpolated_img = closest_neighboor(img, scale_factor=scale_factor)

cv2.imshow('source img', img)
cv2.imshow('interpolated img', interpolated_img)

cv2.waitKey(0)
cv2.destroyAllWindows()