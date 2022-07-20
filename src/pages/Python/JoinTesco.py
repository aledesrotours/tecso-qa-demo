from selenium.webdriver.common.by import By
import time


class JoinTesco:
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
        return self.browser.find_element(By.XPATH, '//*[@id="join"]/div/h1')

    def check_fields(self):
        name_input = 'firstname'
        lastname_input = 'lastname'
        email_input = 'email'
        phone_input = 'phone'
        linkedin_input = 'linkedin'
        login_submit = '//*[@id="apply"]/div[2]/button'

        inputs = ['name', 'lastname', 'email@email.com', 'phone', 'linkedin']

        self.browser.find_element_by_id(name_input).send_keys(inputs[0])
        self.browser.find_element_by_id(lastname_input).send_keys(inputs[1])
        self.browser.find_element_by_id(email_input).send_keys(inputs[2])
        self.browser.find_element_by_id(phone_input).send_keys(inputs[3])
        self.browser.find_element_by_id(linkedin_input).send_keys(inputs[4])
        self.browser.find_element_by_xpath(login_submit).click()
        time.sleep(5)
        return self.browser.find_element_by_xpath('//*[@id="formContact"]/div/h4')
