import unittest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.SearchUsuarioPage import SearchUsuarioPage


class TestCase7(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login_and_search_user(self):
        login_page = LoginPage(self.driver)
        search_usuario_page = SearchUsuarioPage(self.driver)

        login_page.open_login_page()
        self.assertTrue(login_page.is_url_login(), "Falha ao logar na página")

        login_page.exec_login()


        search_usuario_page.go_to_admin_page()

        self.assertTrue(search_usuario_page.is_user_on_admin_page(), "Falha ao navegar para a página de admin")
        search_usuario_page.search_user("Admin")
        self.assertTrue(search_usuario_page.is_user_found("Admin"), "Falha ao navegar para o usuario admin")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
