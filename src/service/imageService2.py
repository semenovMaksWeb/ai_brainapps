import cv2 as cv
import numpy as np


class ImageService2:

    # Обводить все объекты на изображении
    def outlineImage(path_file):
        # параметры цветового фильтра
        hsv_min = np.array((2, 28, 65), np.uint8)
        hsv_max = np.array((26, 238, 255), np.uint8)
        img = cv.imread(path_file)

        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) # меняем цветовую модель с BGR на HSV 
        thresh = cv.inRange(hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
        # ищем контуры и складируем их в переменную contours
        contours, hierarchy = cv.findContours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # отображаем контуры поверх изображения
        cv.drawContours(img, contours, -1, (255,0,0), 3, cv.LINE_AA, hierarchy, 1 )
        cv.imshow('contours', img) # выводим итоговое изображение в окно

        cv.waitKey()
        cv.destroyAllWindows()

    # Обрезать изображение
    def splitImage(path_file, y, x, h, w):
        img = cv.imread(path_file)
        crop_img = img[y:y+h, x:x+w]
        return crop_img

    # Найти изображение в изображение без учитывание его угла положения
    def findObjectImage(path_image, path_template):
        img = cv.imread(path_image)
        template = cv.imread(path_template)
        print(template)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        y1 = top_left[1]
        y2 = bottom_right[1]
        x1 = top_left[0]
        x2 = bottom_right[0]
        # cv.imshow('contours', img[y1:y2, x1:x2]) # выводим итоговое изображение в окно
        # cv.waitKey()
        # cv.destroyAllWindows()
        return img[y1:y2, x1:x2]

    # сохранить изображение
    def saveImage(path_file, bit_image):
        cv.imwrite(path_file, bit_image)