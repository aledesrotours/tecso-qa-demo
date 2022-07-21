import pytest

from src.pages.Python.JoinTecso import JoinTesco


def test_menu_is_display(browser):
    home_page = JoinTesco(browser)
    menu = home_page.click_menu()
    assert menu.is_displayed()


def test_home_is_display(browser):
    home_page = JoinTesco(browser)
    menu = home_page.menu_is_display()
    assert menu.is_displayed()


def test_our_offices(browser):
    home_page = JoinTesco(browser)
    home_page.click_menu()
    our_offices = home_page.search_our_offices()
    assert our_offices.is_displayed()


def test_terms_of_use(browser):
    home_page = JoinTesco(browser)
    home_page.terms_of_use()
    menu = home_page.menu_is_display()
    assert menu.is_displayed()


def test_social_media_linkedin(browser):
    home_page = JoinTesco(browser)
    linkedin_page = home_page.open_li()
    assert linkedin_page.check_linkedin()


def test_social_media_twitter(browser):
    home_page = JoinTesco(browser)
    twitter_page = home_page.open_tw()
    assert twitter_page.check_twitter()


def test_social_media_facebook(browser):
    home_page = JoinTesco(browser)
    facebook_page = home_page.open_fb()
    assert facebook_page.check_facebook()


def test_social_media_instagram(browser):
    home_page = JoinTesco(browser)
    instagram_page = home_page.open_ig()
    assert instagram_page.check_instagram()
