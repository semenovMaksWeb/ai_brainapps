import mss

import numpy as np

class ScreenService:
    def screenshot(path_file):
        with mss.mss() as sct:
            sct.shot(output = path_file)