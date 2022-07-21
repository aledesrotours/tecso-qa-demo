from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LinkedinPage:
    def __init__(self, browser):
        self.browser = browser

    def check_linkedin(self):
        try:
            self.browser.find_element(By.LINK_TEXT, 'Cooperativa de Trabajo TECSO Ltda.')
        except NoSuchElementException:
            return False
        return True
