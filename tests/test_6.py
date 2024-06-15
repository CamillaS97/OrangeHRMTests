import unittest

from selenium import webdriver

from pages.LoginPage import LoginPage
from pages.MyInfoPage import MyInfoPage
from pages.UserPage import UserPage


class TestCase6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_procurar_usuario(self):
        login_page = LoginPage(self.driver)
        user_page = UserPage(self.driver)
        my_info_page = MyInfoPage(self.driver)
        login_page.open_login_page()
        login_page.exec_login()
        user_page.open_side_menu_option_my_info('My Info')
        my_info_page.edit_employee_name('Robson', 'Souza')
        user_page.open_side_menu_option_my_info('My Info')
        self.assertTrue(my_info_page.is_name_title_found('Robson Souza'), "O nome não foi alterado")


if __name__ == "__main__":
    unittest.main()