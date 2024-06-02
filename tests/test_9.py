import unittest
from selenium import webdriver

from pages.EditUserPage import EditUserPage
from pages.LoginPage import LoginPage


class TestEditUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_edit_user_first_name(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.exec_login()

        # Acessar a página de edição do usuário com ID 1
        edit_user_page = EditUserPage(self.driver)
        edit_user_page.open_edit_page()
        edit_user_page.edit_user_first_name("Novo 2")

if __name__ == "__main__":
    unittest.main()
