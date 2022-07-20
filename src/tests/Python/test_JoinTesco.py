from src.pages.Python.JoinTesco import JoinTesco
import unittest
import selenium


def test_JoinTesco(browser):
    home_page = JoinTesco(browser)
    home_page.load()
    menu = home_page.click_menu()
    assert menu.is_displayed()

    menu_jobs = home_page.click_menu_join()
    assert menu_jobs.is_displayed()

    jobs_button = home_page.click_button_join()
    assert jobs_button.is_displayed()

    submit_button = home_page.check_fields()
    assert submit_button.is_displayed()






