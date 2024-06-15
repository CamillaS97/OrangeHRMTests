import unittest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.UserPage import UserPage
from pages.PIMPage import PIMPage


class TestCase5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_procurar_usuario(self):
        login_page = LoginPage(self.driver)
        user_page = UserPage(self.driver)
        pim_page = PIMPage(self.driver)
        login_page.open_login_page()
        login_page.exec_login()
        user_page.open_side_menu_option('PIM')
        pim_page.search_employee('Amelia')
        self.assertTrue(pim_page.is_searched_employee_found('Amelia'), "O usuário não foi encontrado")


if __name__ == "__main__":
    unittest.main()