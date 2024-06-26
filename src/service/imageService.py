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
        return locations
    
    def seacrhColorImages(url_image, color):
        img = cv2.imread(url_image)
        for row in img:
            for pixel in row:
                if pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]: 
                    return True
        return False