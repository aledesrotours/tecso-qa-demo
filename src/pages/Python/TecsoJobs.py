import time

from selenium.common.exceptions import NoSuchElementException

from src.pages.Python.JobsJava import JobsJava


class TecsoJobs:
    def __init__(self, browser):
        self.browser = browser
        self.path_title = '//*[@id="join"]/div/ol/li[2]'

    def check_exists_by_xpath(self):
        try:
            self.browser.find_element_by_xpath(self.path_title)
        except NoSuchElementException:
            return False
        return True

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

    def check_java(self):
        self.browser.find_element_by_xpath('//*[@id="jobs"]/div[1]/div/div[1]/a').click()
        time.sleep(3)
        return JobsJava(self.browser)




