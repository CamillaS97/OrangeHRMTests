import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.UserPage import UserPage


def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help="Select browser")


@pytest.fixture()
def setup(request):
    selected_browser = request.config.getoption('--browser_selenium')
    login_page = LoginPage(browser=selected_browser)
    login_page.open_login_page()
    yield login_page
    login_page.close()


@pytest.fixture()
def login_app(setup):
    login_page = setup
    login_page.exec_login()
    user_page = UserPage(driver=login_page.driver)
    assert user_page.is_dashboard_page(), 'Página não logada corretamente'
    yield login_page, user_page