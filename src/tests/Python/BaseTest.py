import pytest
import selenium.webdriver


@pytest.fixture
def browser():

    chrome_driver = selenium.webdriver.Chrome()

    # Make its calls wait for elements to appear
    chrome_driver.implicitly_wait('5')

    # Return the WebDriver instance for the setup
    yield chrome_driver

    # Quit the WebDriver instance for the cleanup
    chrome_driver.quit()
