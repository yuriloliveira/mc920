import numpy as np
import message_utils as mes

def codify(img, message, bitplan=0):
    if bitplan is None:
        bitplan = 0

    res = np.array(img).flatten()
    b_msg = mes.to_bit_array(message)
    b_msg_len = b_msg.shape[0]
    target_slice = np.array(res[:b_msg_len])
    set_zeros_in_bitplan(target_slice, b_msg == 0, bitplan)
    set_ones_in_bitplan(target_slice, b_msg == 1, bitplan)
    res[:b_msg_len] = target_slice
    return res.reshape(img.shape)

def set_zeros_in_bitplan(arr, cond, bitplan):
    arr[cond] = (arr & ~(1 << bitplan))[cond]

def set_ones_in_bitplan(arr, cond, bitplan):
    arr[cond] = (arr | (1 << bitplan))[cond]

def as_bin_array(arr):
    res = []
    for val in arr:
        res.append('{0:b}'.format(val))
    return res