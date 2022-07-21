from selenium.webdriver.common.by import By
from src.pages.Python.PrivacyPolicy import PrivacyPolicyPage


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://tecso.coop/'
    def load(self):
        self.browser.get(self.url)
    def click_menu(self):
        element_menu = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div[2]/label')
        self.browser.find_element(*element_menu).click()
        return self.browser.find_element(By.ID, '#nav-main')
    def click_menu_contactus(self):
        self.contact_us_button=self.browser.find_element(By.XPATH,'//*[@id="#nav-main"]/div/div[4]/a[3]/h3')
        self.contact_us_button.click()
        return self.browser.current_url
    def click_menu_associations(self):
        self.associations_button=self.browser.find_element(By.XPATH,'//*[@id="#nav-main"]/div/div[3]/a[4]/h3')
        self.associations_button.click()
        return self.browser.current_url
    def get_mails_contactus(self):
        contact_mail=self.browser.find_element(By.XPATH,'//*[@id="cform"]/div/div/div[1]/div/div[2]/a[1]')
        join_mail=self.browser.find_element(By.XPATH,'//*[@id="cform"]/div/div/div[1]/div/div[2]/a[2]')
        return [contact_mail.text,join_mail.text]
    def fill_info_contactus(self,datos):
        name_entry=self.browser.find_element(By.XPATH,'//*[@id="cform"]/div/div/div[2]/form/ul/li[1]/input')
        mail_entry=self.browser.find_element(By.XPATH,'//*[@id="cform"]/div/div/div[2]/form/ul/li[2]/input')
        coop_entry=self.browser.find_element(By.XPATH,'//*[@id="cform"]/div/div/div[2]/form/ul/li[3]/input')
        mess_entry=self.browser.find_element(By.TAG_NAME,'textarea')
        send_button=self.browser.find_element(By.XPATH,'//*[@id="cform"]/div/div/div[2]/form/ul/li[4]/button')

        for input,dato in zip([name_entry,mail_entry,coop_entry,mess_entry],datos):
            input.send_keys(dato)

        send_button.click()

        return self.browser.find_element(By.XPATH,'//*[@id="cform"]/div/div/div[2]/h2').is_displayed(),
    def click_es_button(self):
        self.browser.find_element(By.XPATH,'//*[@id="navbar"]/div/nav/span/a[1]/span').click()
        return self.browser.current_url
    def click_en_button(self):
        self.browser.find_element(By.XPATH,'//*[@id="navbar"]/div/nav/span/a[2]/span').click()
        return self.browser.current_url
    def click_privacy_policy(self):
        self.browser.find_element(By.XPATH,'//*[@id="contact"]/div/div/div[4]/p/a[2]').click()
        return PrivacyPolicyPage(self.browser)
