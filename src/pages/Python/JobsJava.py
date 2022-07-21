from selenium.common.exceptions import NoSuchElementException


class JobsJava:
    def __init__(self, browser):
        self.browser = browser
        self.path_title = '//*[@id="job"]/div[2]/p[2]/strong'

    def check_exists_by_xpath(self):
        try:
            self.browser.find_element_by_xpath(self.path_title)
        except NoSuchElementException:
            return False
        return True
