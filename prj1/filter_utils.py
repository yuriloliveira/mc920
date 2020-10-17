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
    show_src_and_filtered_image(src_image, filtered_image, 'source image / filtered image (mask = ' + mask_id + ')')

    other_mask_id = 'h4' if mask_id == 'h3' else 'h3' if mask_id == 'h4' else None

    if (other_mask_id):
        other_filtered_image = filter_image(src_image, other_mask_id)
        combined_filters_image = add_filters(filtered_image, other_filtered_image)
        show_src_and_filtered_image(
            src_image,
            combined_filters_image,
            'source image / combination of h3 and h4 masks'
        )
        return (filtered_image, other_filtered_image)
    
    return (filtered_image, None)

def show_src_and_filtered_image(src_image, filtered_image, title=''):
    result = np.hstack((src_image, filtered_image))
    cv2.imshow(title, result) 

def filter_image(src_image, mask_id, borderType=cv2.BORDER_REPLICATE):
    return cv2.filter2D(src_image, -1, get_mask(mask_id), borderType=borderType)

def add_filters(img1, img2):
    added_filer_image = (img1.astype(float)**2 + img2.astype(float)**2) ** (1/2)
    return cv2.normalize(
        added_filer_image,
        None,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX,
        dtype=cv2.CV_32F
    ).astype(np.uint8)