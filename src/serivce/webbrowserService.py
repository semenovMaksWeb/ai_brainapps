from config import urlSite

import webbrowser

class WebbrowserService:
    def open(url):
        webbrowser.open(url = urlSite + url)