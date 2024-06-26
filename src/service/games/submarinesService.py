from service.screenService import ScreenService
from service.imageService import ImageService
from service.actionService import ActionService
from service.webbrowserService import WebbrowserService
from config import screenSave

import time

class SubmarinesService:
    url = "https://brainapps.ru/game/play/Submarine"
    submarinesImage = "submarines.png"
    colorGreen = (61, 252, 140)
    colorOrange = (65, 180, 250)         

    def start():
        WebbrowserService.open("game/play/Submarine")
        time.sleep(2)
        ActionService.clickRunButton()
        time.sleep(5)
        ScreenService.screenshot(SubmarinesService.submarinesImage)
        checkColor = SubmarinesService.checkColorSubmarines()

        if checkColor == "orange":
            position = SubmarinesService.definePosition()
            ActionService.keyDown(position)
        if checkColor == "green":
            pass

    def checkColorSubmarines():
        checkColorGreen = ImageService.seacrhColorImages(
            screenSave + SubmarinesService.submarinesImage, 
            SubmarinesService.colorGreen
        )
        if checkColorGreen:
            return "green"
        return "orange"
    
    def definePosition():
        checkTop = ImageService.comparisonImages(
            screenSave + SubmarinesService.submarinesImage, 
            screenSave + "const/submarines/orangeTop.png"
        )
        if len(checkTop) != 0:
            return "top"
            
        checkBottom = ImageService.comparisonImages(
            screenSave + SubmarinesService.submarinesImage, 
            screenSave + "const/submarines/orangeBottom.png"
        )
        if len(checkBottom) != 0:
            return "bottom"

        checkLeft = ImageService.comparisonImages(
            screenSave + SubmarinesService.submarinesImage, 
            screenSave + "const/submarines/orangeLeft.png"
        )
        if len(checkLeft) != 0:
            return "left"
    
        checkRight = ImageService.comparisonImages(
            screenSave + SubmarinesService.submarinesImage, 
            screenSave + "const/submarines/orangeRight.png"
        )
        if len(checkRight) != 0:
            return "right"
        
    def defineDirection():
        pass