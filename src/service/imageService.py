import cv2
import numpy as np

class ImageService:
    def comparisonImages(urlImageFind, urlImageFrom, type = cv2.TM_CCOEFF_NORMED):
        findImage = cv2.imread(urlImageFind)
        fromImage = cv2.imread(urlImageFrom)
        result = cv2.matchTemplate(findImage, fromImage, type)
        threshold = 0.8
        locations = []
        for y, x in zip(*np.where(result >= threshold)):
            locations.append((x, y)) 
        return locations
    
    def findColorImage(urlImage, color):
        img = cv2.imread(urlImage)
        for indexRow, row in enumerate(img):
            for indexPixel, pixel in enumerate(row):
                print(pixel)
                if pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]: 
                    return indexRow, indexPixel
        return None
    
    # Обрезать изображение
    def splitImage(path_file, y, x, h, w):
        img = cv2.imread(path_file)
        crop_img = img[y:y+h, x:x+w]
        return crop_img
    
    # сохранить изображение
    def saveImage(path_file, bit_image):
        cv2.imwrite(path_file, bit_image)