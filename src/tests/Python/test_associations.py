from src.pages.Python.HomePage import HomePage

def test_associations(browser):
    # GIVEN: Tecso Coop homepage
    
    # WHEN:  User clicks on menu button
    # THEN:  Menu displays

    # WHEN:  User Clicks on 'Associations' section
    # THEN:  Autoscroll to 'Associations' section

    homepage=HomePage(browser)
    homepage.load()

    menu = homepage.click_menu()
    assert menu.is_displayed()

    associations_url=homepage.click_menu_associations()
    assert "partners" in associations_url
