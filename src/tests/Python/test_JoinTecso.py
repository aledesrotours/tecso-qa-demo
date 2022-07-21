from src.pages.Python.JoinTecso import JoinTecso
import unittest
import selenium


def test_JoinTecso(browser):
    home_page = JoinTecso(browser)
    home_page.load()
    menu = home_page.click_menu()
    assert menu.is_displayed()

    menu_jobs = home_page.click_menu_join()
    assert menu_jobs.is_displayed()

    jobs_button = home_page.click_button_join()
    assert jobs_button.check_exists_by_xpath()

    assert jobs_button.check_fields()

def test_ClientsTecso(browser):
    home_page = JoinTecso(browser)
    home_page.load()
    clients_button = home_page.click_menu_client()
    assert clients_button.is_displayed()

def test_JoinTecso_java(browser):

    home_page = JoinTecso(browser)
    home_page.load()
    menu = home_page.click_menu()
    assert menu.is_displayed()

    menu_jobs = home_page.click_menu_join()
    assert menu_jobs.is_displayed()

    jobs_button = home_page.click_button_join()
    assert jobs_button.check_exists_by_xpath()
    assert jobs_button.check_java()












