import numpy as np
import bitarray

BYTE_SIZE = 8
def decodify(img, bitplan=0):
    if bitplan is None:
        bitplan = 0
    
    msg_len = 88
    byte_count = int(msg_len / BYTE_SIZE)
    msg_slice = np.array(img).flatten()[:msg_len]
    bit_msg = np.array((msg_slice & (1 << bitplan)) >> bitplan, dtype=np.byte).reshape(byte_count, BYTE_SIZE)
    return np.packbits(bit_msg, axis=-1).reshape(byte_count).tostring()