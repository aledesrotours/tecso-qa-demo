

class JoinTesco:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://tecso.coop/'

    def load(self):
        self.browser.get(self.url)