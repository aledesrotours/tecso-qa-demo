from src.pages.Python.JoinTesco import JoinTesco


def test_JoinTesco(browser):
    home_page = JoinTesco(browser)
    home_page.load()