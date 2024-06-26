from serivce.webbrowserService import WebbrowserService
from serivce.actionService import ActionService

import time

def start():
    WebbrowserService.open("game/play/Submarine")
    time.sleep(2)
    ActionService.clickRunButton()
start()