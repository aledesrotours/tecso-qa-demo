import pytest
import selenium.webdriver


@pytest.fixture
def browser():


    chrome_driver = selenium.webdriver.Chrome()

    chrome_driver.implicitly_wait('10')

    # Return the WebDriver instance for the setup
    yield chrome_driver

    # Quit the WebDriver instance for the cleanup
    chrome_driver.quit()
