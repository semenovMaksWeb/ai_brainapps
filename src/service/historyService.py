import cv2 as cv
from config import screenSave
from datetime import datetime

import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

class HistoryService:
    def saveImg(bit_img, img_name):
        str =  screenSave + "history/" + img_name + randomword(10) + ".png"
        print(str)
        cv.imwrite(str, bit_img)