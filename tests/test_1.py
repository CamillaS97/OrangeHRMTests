import time

from pages.LoginPage import LoginPage


class TestCase1:

    def test_efetuar_login(self, login_app):
        login_page, user_page = login_app
        user_page.open_side_menu_option('Recruitment')

        time.sleep(10)
        assert True