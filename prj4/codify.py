import message_utils as mes

def codify(img, message):
    bit_message = mes.to_bit_array(message)
    return img