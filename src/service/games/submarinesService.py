from service.screenService import ScreenService
from service.imageService import ImageService
from service.imageService2 import ImageService2
from service.actionService import ActionService
from service.webbrowserService import WebbrowserService
from service.historyService import HistoryService
from config import screenSave

import time

class SubmarinesService:
    url = "https://brainapps.ru/game/play/Submarine"
    submarinesImage = screenSave + "generator/submarines.png"
    submarinesTemplate = screenSave + "const/submarines/submarinesTemplate.png"
    submarinesImagePole = screenSave + "generator/pole.png"
    submarinesImageElement = "generator/submarinesElement.png"
    colorGreen = (61, 252, 140)
    colorOrange = (65, 180, 250) 
    colorPosition = (167,167,167)
    
    def start():
        # WebbrowserService.open("game/play/Submarine")
        # time.sleep(5)
        # ActionService.clickRunButton()
        # time.sleep(5)
        while(True):
            time.sleep(1)
            # ScreenService.screenshot(SubmarinesService.submarinesImage)
            checkRestart = ActionService.checkButtonRestart(SubmarinesService.submarinesImage)
            if checkRestart: 
                break
            SubmarinesService.generatorImagePole()
            image = SubmarinesService.findImageHead()
            print("image [0][0] and [0][1]", image[0][0], image[0][0])
            HistoryService.saveImg(image, "find_submarines")
            key = None
            if image[0][0] == 127 or image[0][0] == 134:
                key = "up"
            if image[0][0] == 146:
                key = "left"
            if image[0][0] == 63:
                key = "down"
            if image[0][0] == 187 or image[0][0] == 180:
                key = "right"
            if key is None:
                print("bag click - up")
                key = "up"
            print(key)
            ActionService.keyDown(key)

    # создает обрезанное поле
    def generatorImagePole():
        image = ImageService2.splitImage(
            path_file = SubmarinesService.submarinesImage,
            h = 480,
            w = 1800,
            x = 0,
            y = 250
        )
        ImageService2.saveImage(SubmarinesService.submarinesImagePole, image)

    # Поиск изображении
    def findImageHead():
        return ImageService2.findObjectImage(SubmarinesService.submarinesImagePole, SubmarinesService.submarinesTemplate)


    def start2():
        # WebbrowserService.open("game/play/Submarine")
        # time.sleep(2)
        # ActionService.clickRunButton()
        # time.sleep(5)
        # while(True):
            time.sleep(1)
            # ScreenService.screenshot(SubmarinesService.submarinesImage)
            checkRestart = ActionService.checkButtonRestart(SubmarinesService.submarinesImage)
            print("checkRestart", checkRestart)
            # if checkRestart: 
                # break
            
            checkColor = SubmarinesService.checkColorSubmarines()
            print("checkColor", checkColor)
            if checkColor == "orange":
                print("orange")
                position = SubmarinesService.definePosition()
                ActionService.keyDown(position)
            if checkColor == "green":
                print("green")
                # TODO Времянка
                ActionService.keyDown("top")

    def checkColorSubmarines():
        checkColorGreen = ImageService.seacrhColorImages(
            screenSave + SubmarinesService.submarinesImage, 
            SubmarinesService.colorGreen
        )
        if checkColorGreen:
            return "green"
        return "orange"
    
    def definePosition():
        # TODO дописать функцию
        ImageService.getImages(
            screenSave + SubmarinesService.submarinesImage, 
            screenSave + "const/submarines/top.png",
            screenSave + SubmarinesService.submarinesImageElement,
        )

        position = ImageService.getColorImagesPosition(
            url_image= screenSave + SubmarinesService.submarinesImageElement,
            color = SubmarinesService.colorPosition
        )
        print(position)
        #  (0, 29) TOP
        #  (9, 53) RIGHT
        # (8, 16) BOTTOM
        # (16, 11) LEFT

        if position[0] >= 7:
            return "up"
        
        if position[1] >= 11:
            return "right"
        
        if position[0] <= 8:
            return "bottom"
        
        if position[1] <= 20:
            return "left"   

    def defineDirection():
        pass