from os import listdir
import cv2
from codify import codify
from decodify import decodify

for text_file_path in listdir('./text'):
    for img_path in listdir('./images'):
        for bitplan in range(0, 3):
            try:
                img = cv2.imread("./images/" + img_path, cv2.IMREAD_COLOR)
                msg = open("./text/" + text_file_path).read()
                res_img = codify(img, msg, bitplan=bitplan)
                decodified_msg = decodify(res_img, bitplan=bitplan)
                if msg == decodified_msg:
                    print("[OK] {} {} {}".format(text_file_path, img_path, bitplan))
                else:
                    print('[Failed] {} {} {} ("{}" != "{}")'.format(text_file_path, img_path, bitplan, msg, decodified_msg))
            except Exception as ex:
                print("[Failed] An exception ocurred during execution of {} {} {}:".format(text_file_path, img_path, bitplan))
                print(ex)
        