import message_utils as mes

def codify(img, message, bitplan=0):
    bit_message = mes.to_bit_array(message)
    return img