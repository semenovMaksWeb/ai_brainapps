import cv2
import numpy as np


class ImageService:
    #  возвращает координаты
    def getGrayImagesPosition(url_image_find = None, url_image_from = None, bit_image_find = None, bit_image_from = None):
        if bit_image_find and bit_image_find.all(): 
            findImage = bit_image_find
        else:
            findImage = cv2.imread(url_image_find, cv2.IMREAD_GRAYSCALE)
        
        if bit_image_from and bit_image_from.all(): 
            fromImage = bit_image_from
        else:
            fromImage = cv2.imread(url_image_from, cv2.IMREAD_GRAYSCALE)
          
        w, h = fromImage.shape[::-1]
        result = cv2.matchTemplate(findImage, fromImage, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        y1 = top_left[1]
        y2 = bottom_right[1]
        x1 = top_left[0]
        x2 = bottom_right[0]
        return ( y1, y2, x1, x2 )


    #  возвращает изображение учитывая цвет, все конвертируется в серый оттенок
    def getGrayImages(url_image_find, url_image_from):
        findImage = cv2.imread(url_image_find, cv2.IMREAD_GRAYSCALE)
        fromImage = cv2.imread(url_image_from, cv2.IMREAD_GRAYSCALE)
        w, h = fromImage.shape[::-1]
        result = cv2.matchTemplate(findImage, fromImage, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        y1 = top_left[1]
        y2 = bottom_right[1]
        x1 = top_left[0]
        x2 = bottom_right[0]
        return findImage[y1:y2, x1:x2]

    def showImage(image):
        cv2.imshow("Image", image)
        cv2.waitKey(0)

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