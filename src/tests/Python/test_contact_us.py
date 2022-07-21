from src.pages.Python.HomePage import HomePage


def test_contact_us(browser):
    # GIVEN: Tecso Coop homepage

    # WHEN:  User clicks on menu button
    # THEN:  Menu displays

    # WHEN:  User Clicks on 'Contact Us' section
    # THEN:  Autoscroll to 'Contact Us' section
    # AND:   Contact's mails are displayed

    # WHEN:  User fill information in inputs
    # THEN:  Confirmation message appears


    homepage=HomePage(browser)
    homepage.load()
    
    menu = homepage.click_menu()
    assert menu.is_displayed()

    contact_us_url =  homepage.click_menu_contactus()
    assert "contact" in contact_us_url

    mails=homepage.get_mails_contactus()
    for mail in mails:
        assert "@" and "." in mail

    datos=["Nombre Apellido","email_generico@email.com","NN-Coop","Mensaje de prueba"]
    ok=homepage.fill_info_contactus(datos)
    assert ok