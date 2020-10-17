import numpy as np
import cv2
from matplotlib import pyplot as plt
from masks import get_mask, get_all_masks_ids

def plot_filtered_image(src_image, mask_id):
    filtered_image = filter_image(src_image, mask_id)
    fig, ax = plt.subplots(1,2)
    plt.title('mask=' + mask_id)
    ax[0].imshow(src_image)
    ax[1].imshow(filtered_image)

def plot_filtered_images(src_image, mask_ids):
    for mask_id in mask_ids:
        plot_filtered_image(src_image, mask_id)

def show_filtered_image(src_image, mask_id):
    filtered_image = filter_image(src_image, mask_id)
    result = np.hstack((src_image, filtered_image))
    cv2.imshow('Source image / filtered image (mask = ' + mask_id + ')', result)

def filter_image(src_image, mask_id, borderType=cv2.BORDER_REPLICATE):
    return cv2.filter2D(src_image, -1, get_mask(mask_id), borderType=borderType)