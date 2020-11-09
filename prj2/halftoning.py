import cv2
import numpy as np 
from utils import floyd_stein

img = cv2.imread('images/baboon.png', cv2.IMREAD_COLOR)
res_img = floyd_stein(np.array(img))

cv2.imshow('source image', img)
cv2.imshow('resulting image', res_img)

cv2.waitKey(0)
cv2.destroyAllWindows()