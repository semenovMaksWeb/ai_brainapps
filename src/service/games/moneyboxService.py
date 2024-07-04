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
    pathMany = screenSave + "const/moneybox/many.png"

    def start():
        WebbrowserService.open("game/play/PiggyBank")
        time.sleep(3)
        ScreenService.screenshot(MoneyboxService.pathLevelScreen)
        ActionService.clickRunButton()
        time.sleep(2)
        ScreenService.screenshot(MoneyboxService.pathLevelScreen)
        MoneyboxService.findLevel()
        time.sleep(5)
        MoneyboxService.runGames()
        pass

    def runGames():
        ScreenService.screenshot(MoneyboxService.pathLevelScreen)
        locations = ImageService.comparisonImages(MoneyboxService.pathLevelScreen, MoneyboxService.pathMany)
        print(locations)

    def findLevel():
        locations = ImageService.comparisonImages(MoneyboxService.pathLevelScreen, MoneyboxService.pathLevelTemplate)
        x = locations[0][0] + 15
        y = locations[0][1] + 15
        ActionService.move(x, y)
        ActionService.click()
        pass