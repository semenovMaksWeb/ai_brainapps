from service.screenService import ScreenService
from service.imageService import ImageService
from service.actionService import ActionService
from service.webbrowserService import WebbrowserService
from config import screenSave

import time

class SubmarinesService:
    url = "https://brainapps.ru/game/play/Submarine"
    submarinesImage = "generator/submarines.png"
    submarinesImageElement = "generator/submarinesElement.png"
    colorGreen = (61, 252, 140)
    colorOrange = (65, 180, 250) 
    colorPosition = (167,167,167)       

    def start():
        WebbrowserService.open("game/play/Submarine")
        time.sleep(2)
        ActionService.clickRunButton()
        time.sleep(5)
        while(True):
            time.sleep(2)
            ScreenService.screenshot(SubmarinesService.submarinesImage)
            checkRestart = ActionService.checkButtonRestart("generator/submarines.png")
            print("checkRestart", checkRestart)
            if checkRestart: 
                break
            
            checkColor = SubmarinesService.checkColorSubmarines()
            print("checkColor", checkColor)
            if checkColor == "orange":
                position = SubmarinesService.definePosition()
                ActionService.keyDown(position)
            if checkColor == "green":
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
        ImageService.getGrayImages(
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