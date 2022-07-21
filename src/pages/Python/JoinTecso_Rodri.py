import time

from selenium.webdriver.common.by import By

from src.pages.Python.facebook import FacebookPage
from src.pages.Python.instagram import InstagramPage
from src.pages.Python.linkedin import LinkedinPage
from src.pages.Python.twitter import TwitterPage


class JoinTesco:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://tecso.coop/'
        self.browser.get(self.url)

    def click_menu(self):
        element_menu = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[2]/label')
        self.browser.find_element(*element_menu).click()
        time.sleep(2)
        return self.browser.find_element(By.ID, '#nav-main')

    def menu_is_display(self):
        return self.browser.find_element(By.XPATH, '//*[@id="__layout"]/div/div/header/div/div/div/h2')

    def search_our_offices(self):
        element_our_offices = (By.XPATH, '//*[@id="#nav-main"]/div/div[4]/a[1]/h3')
        self.browser.find_element(*element_our_offices).click()
        time.sleep(2)
        return self.browser.find_element(By.XPATH, '//*[@id="locations"]/div/h1')

    def terms_of_use(self):
        element_our_offices = (By.XPATH, '//*[@id="contact"]/div/div/div[4]/p/a[1]')
        self.browser.find_element(*element_our_offices).click()
        element_menu = (By.PARTIAL_LINK_TEXT, 'Home')
        time.sleep(3)
        self.browser.find_element(*element_menu).click()

    def open_li(self):
        element_li = (By.XPATH, '//*[@id="__layout"]/div/div/header/div/div/div/div/a[1]')
        self.browser.find_element(*element_li).click()
        return LinkedinPage(self.browser)

    def open_tw(self):
        element_tw = (By.XPATH, '//*[@id="__layout"]/div/div/header/div/div/div/div/a[3]')
        self.browser.find_element(*element_tw).click()
        return TwitterPage(self.browser)

    def open_fb(self):
        element_fb = (By.XPATH, '//*[@id="__layout"]/div/div/header/div/div/div/div/a[2]')
        self.browser.find_element(*element_fb).click()
        return FacebookPage(self.browser)

    def open_ig(self):
        element_our_ig = (By.XPATH, '//*[@id="__layout"]/div/div/header/div/div/div/div/a[4]')
        self.browser.find_element(*element_our_ig).click()
        return InstagramPage(self.browser)
