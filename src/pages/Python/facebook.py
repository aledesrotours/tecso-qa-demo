from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class FacebookPage:
    def __init__(self, browser):
        self.browser = browser

    def check_facebook(self):
        try:
            self.browser.find_element(By.LINK_TEXT, 'Cooperativa de Trabajo TECSO ltda.')
        except NoSuchElementException:
            return False
        return True
