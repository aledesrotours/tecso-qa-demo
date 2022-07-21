from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TwitterPage:
    def __init__(self, browser):
        self.browser = browser

    def check_twitter(self):
        try:
            self.browser.find_element(By.LINK_TEXT, '@tecsocoop')
        except NoSuchElementException:
            return False
        return True
