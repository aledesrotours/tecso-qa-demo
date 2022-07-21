from selenium.webdriver.common.by import By
import time


class PrivacyPolicyPage:
    def __init__(self, browser):
        self.browser = browser
    def check_pp_page(self):
        a=self.browser.find_element(By.XPATH,'//*[@id="locations"]/div/h1[1]').is_displayed()
        return a
    def click_home(self):
        time.sleep(5)
        self.browser.find_element(By.XPATH,'//*[@id="locations"]/div/ol/li[1]/a').click()
        from src.pages.Python.HomePage import HomePage
        return HomePage(self.browser)