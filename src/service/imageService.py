import cv2
import numpy as np

class ImageService:
    def comparisonImages(url_image_find, url_image_from, type = cv2.TM_CCOEFF_NORMED):
        findImage = cv2.imread(url_image_find)
        fromImage = cv2.imread(url_image_from)
        result = cv2.matchTemplate(findImage, fromImage, type)
        threshold = 0.8
        locations = []
        for y, x in zip(*np.where(result >= threshold)):
            locations.append((x, y)) 
        return locations