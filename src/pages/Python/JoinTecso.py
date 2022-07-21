from selenium.webdriver.common.by import By
import time

from src.pages.Python.TecsoJobs import TecsoJobs


class JoinTecso:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://tecso.coop/'

    def load(self):
        self.browser.get(self.url)

    def click_menu(self):
        element_menu = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[2]/label')
        self.browser.find_element(*element_menu).click()
        time.sleep(5)
        return self.browser.find_element(By.ID, '#nav-main')

    def click_menu_join(self):
        element_join_section = (By.XPATH, '//*[@id="#nav-main"]/div/div[4]/a[2]')
        self.browser.find_element(*element_join_section).click()
        return self.browser.find_element(By.XPATH, '//*[@id="joinus"]/div/h1')

    def click_button_join(self):
        element_join_button = (By.XPATH, '//*[@id="joinus"]/div/div/a')
        self.browser.find_element(*element_join_button).click()
        time.sleep(3)
        return TecsoJobs(self.browser)

    def click_menu_client(self):
        element_menu = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[2]/label')
        self.browser.find_element(*element_menu).click()
        element_client_section = (By.XPATH, '//*[@id="#nav-main"]/div/div[3]/a[3]/h3')
        self.browser.find_element(*element_client_section).click()
        return self.browser.find_element(By.XPATH, '//*[@id="clients"]/div/h1')



