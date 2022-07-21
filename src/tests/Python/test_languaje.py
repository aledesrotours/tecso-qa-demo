from src.pages.Python.HomePage import HomePage

def test_languaje_buttons(browser):
    # GIVEN: tecso coop homepage
    
    # WHEN:  Click on 'ES' button
    # THEN:  Go to translasated page (spanish)

    # WHEN: Click on 'EN' button 
    # THEN: Go to translasated page (english)
    
    homepage=HomePage(browser)
    homepage.load()

    es_url=homepage.click_es_button()
    assert es_url=="https://tecso.coop/es"

    en_url=homepage.click_en_button()
    assert en_url=="https://tecso.coop/"
