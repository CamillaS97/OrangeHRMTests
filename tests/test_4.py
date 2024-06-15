import unittest
from pages.LoginPage import LoginPage
from selenium import webdriver
from pages.UserPage import UserPage


class TestCase4(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_procurar_time(self):
        login_page = LoginPage(self.driver)
        user_page = UserPage(self.driver)
        login_page.open_login_page()
        login_page.exec_login()
        user_page.open_side_menu_search('Time')
        self.assertTrue(user_page.is_menu_option_present('Time'), "A opção informada não está disponível no menu")


if __name__ == "__main__":
    unittest.main()
