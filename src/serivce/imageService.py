import cv2
import numpy as np


class ImageService:
    def comparisonImages(url_image_find, url_image_from):
        findImage = cv2.imread(url_image_find)
        fromImage = cv2.imread(url_image_from)
        result = cv2.matchTemplate(findImage, fromImage, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        locations = []
        for y, x in zip(*np.where(result >= threshold)):
            locations.append((x, y))
        print(locations)
        return locations