import mss
from config import screenSave

import numpy as np

class ScreenService:
    def screenshot(path_file):
        with mss.mss() as sct:
            sct.shot(output = screenSave + path_file)