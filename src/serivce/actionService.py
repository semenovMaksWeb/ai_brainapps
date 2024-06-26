from serivce.imageService import ImageService
from serivce.screenService import ScreenService
from config import screenSave

import pyautogui

class ActionService:
    def move(x, y):
        pyautogui.moveTo(x = x, y = y)
    
    def click():
        pyautogui.click()

    # Нажать на кнопку запустить игру
    def clickRunButton():
            image_screen_full = "screen_games.png"
            ScreenService.screenshot(image_screen_full)
            locations = ImageService.comparisonImages(screenSave + image_screen_full, screenSave + "button_run.png")
            x = locations[0][0] + 15
            y = locations[0][1] + 15
            ActionService.move(x, y)
            ActionService.click()
            