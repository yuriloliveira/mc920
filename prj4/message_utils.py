import numpy as np
import bitarray

def to_bit_array(msg):
    ba = bitarray.bitarray()
    ba.frombytes(msg.encode('utf-8'))
    return np.ones(ba.length(), dtype=np.uint8) * ba.tolist() # ba.tolist = list of booleans