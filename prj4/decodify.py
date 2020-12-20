import numpy as np
import bitarray

BYTE_SIZE = 8
def decodify(img, bitplan=0, delimiter_char='@'):
    if bitplan is None:
        bitplan = 00

    max_msg_len = img.shape[0] * img.shape[1] * img.shape[2]
    byte_count = int(max_msg_len / BYTE_SIZE)
    msg_slice = np.array(img).flatten()[:max_msg_len]
    bit_msg = np.array((msg_slice & (1 << bitplan)) >> bitplan, dtype=np.byte).reshape(byte_count, BYTE_SIZE)
    byte_msg = np.packbits(bit_msg, axis=-1).reshape(byte_count)
    return extract_message(byte_msg, delimiter_char).tostring().decode('utf-8')

def extract_message(byte_msg, delimiter_char):
    delimiter = ord(delimiter_char[0])
    delimiter_indexes = np.array(np.where(byte_msg == delimiter))[0]
    delimiters_len = delimiter_indexes.shape[0]
    if delimiters_len < 2:
        raise Exception("Invalid message: too few delimiters found. {} found, but 2 are expected"\
            .format(delimiters_len))
    
    [left, right] = delimiter_indexes[:2]

    return byte_msg[left + 1:right]