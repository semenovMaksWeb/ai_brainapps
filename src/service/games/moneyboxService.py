from service.webbrowserService import WebbrowserService
from service.imageService import ImageService
from service.actionService import ActionService
from service.screenService import ScreenService
from config import screenSave
import time

class MoneyboxService:
    pathLevelScreen = screenSave + "generator/moneybox.png"
    pathPole = screenSave + "generator/moneybox_pole.png"
    pathLevelTemplate = screenSave + "const/moneybox/level.png"

    def start():
        WebbrowserService.open("game/play/PiggyBank")
        time.sleep(5)
        ScreenService.screenshot(MoneyboxService.pathLevelScreen)
        ActionService.clickRunButton()
        ActionService.saveScreen(MoneyboxService.pathLevelScreen, MoneyboxService.pathPole)
        MoneyboxService.findLevel()
        pass

    def findLevel():
        res = ImageService.comparisonImages(MoneyboxService.pathPole, MoneyboxService.pathLevelTemplate)
        print(res)
        pass