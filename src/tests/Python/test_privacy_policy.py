from src.pages.Python.HomePage import HomePage
from src.pages.Python.PrivacyPolicy import PrivacyPolicyPage


def test_privacy_policy(browser):
    #GIVEN: Tecso Coop homepage
    
    #WHEN:  Click on privacy policy
    #THEN:  Be on Privacy policy page
    
    #WHEN:  Click on home button
    #THEN:  Be on homepage

    homepage=HomePage(browser)
    homepage.load()

    pp_page=homepage.click_privacy_policy()
    assert pp_page.check_pp_page()

    homepage=pp_page.click_home()

    homepage_url=homepage.browser.current_url
    assert homepage_url == homepage.url


