import cv2
import numpy as np


class ImageService:
    #  возвращает координаты
    def getGrayImagesPosition(url_image_find = None, url_image_from = None):
        findImage, fromImage = ImageService._getImageCheck(url_image_find,url_image_from)        
        return ImageService._getPositionImage(findImage, fromImage)


    #  возвращает изображение учитывая цвет, все конвертируется в серый оттенок
    def getImages(url_image_find = None, url_image_from = None, path_save = None):
        findImage, fromImage = ImageService._getImageCheck(url_image_find,url_image_from,)
        positon = ImageService._getPositionImage(findImage, fromImage)
        cv2.imwrite(path_save, findImage[positon[0]:positon[1], positon[2]:positon[3]])

    # Проверка отправлен путь к файлу или биты изображения
    def _getImageCheck(url_image_find = None, url_image_from = None, type = cv2.IMREAD_GRAYSCALE):
        fromImage = cv2.imread(url_image_from, type)
        findImage = cv2.imread(url_image_find, type)
        return findImage, fromImage
    
    # получить позицию найденного изображение в изображении
    def _getPositionImage(findImage, fromImage):
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

    def showImage(image):
        cv2.imshow("Image", image)
        cv2.waitKey(0)

    def comparisonImages(url_image_find, url_image_from, type = cv2.TM_CCOEFF_NORMED):
        findImage = cv2.imread(url_image_find)
        fromImage = cv2.imread(url_image_from)
        result = cv2.matchTemplate(findImage, fromImage, type)
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
    
    def getColorImagesPosition(url_image = None, color = None):
        img = cv2.imread(url_image)
        for indexRow, row in enumerate(img):
            for indexPixel, pixel in enumerate(row):
                if pixel[0] == color[0] and pixel[1] == color[1] and pixel[2] == color[2]: 
                    return indexRow, indexPixel
        return None