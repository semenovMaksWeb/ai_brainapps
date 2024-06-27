from service.imageService import ImageService
from service.screenService import ScreenService
from config import screenSave
import keyboard

import pyautogui

class ActionService:
    def move(x, y):
        pyautogui.moveTo(x = x, y = y, duration = 0.25)
    
    def click():
        pyautogui.click()

    # Нажать на кнопку запустить игру
    def clickRunButton():
            image_screen_full = "generator/screen_games.png"
            ScreenService.screenshot(image_screen_full)
            locations = ImageService.comparisonImages(screenSave + image_screen_full, screenSave + "const/button_run.png")
            x = locations[0][0] + 15
            y = locations[0][1] + 15
            ActionService.move(x, y)
            ActionService.click()
    
    def checkButtonRestart(image):
        locations = ImageService.comparisonImages(screenSave + image, screenSave + "const/button_restart.png")
        if len(locations) != 0: 
            return True
        return False
    
    def keyDown(key):     
        keyboard.press(key)