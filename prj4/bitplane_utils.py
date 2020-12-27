import cv2
import numpy as np

def extract_bitplane(img, bitplane, bitlen=8):
    target_index = bitlen - bitplane - 1 
    result = np.unpackbits(img).reshape(img.shape[0], img.shape[1], bitlen)
    result[:, :, 0 : target_index] = 0
    result[:, :, target_index + 1 : bitlen] = 0
    result = np.packbits(result).reshape(img.shape[0], img.shape[1])
    cv2.normalize(result, result, 0, 255, cv2.NORM_MINMAX)
    return result

def extract_rgb_bitplane(img, bitplane, bitlen=8):
    img_blue, img_green, img_red = cv2.split(img)
    img_blue = extract_bitplane(img_blue, bitplane)
    img_green = extract_bitplane(img_green, bitplane)
    img_red = extract_bitplane(img_red, bitplane)
    return (img_blue, img_green, img_red)

def merge_rgb(blue, green, red):
    w, h = blue.shape
    bitplanes_img = np.zeros((w, h, 3))
    bitplanes_img[:, :, 0] = blue
    bitplanes_img[:, :, 1] = green
    bitplanes_img[:, :, 2] = red
    return bitplanes_img