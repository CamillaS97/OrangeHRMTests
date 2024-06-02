import unittest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.OrdenarPage import OrderUsersPage


class TestSortUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_sort_users_by_username_asc(self):
        login_page = LoginPage(self.driver)
        order_users_page = OrderUsersPage(self.driver)

        login_page.open_login_page()
        self.assertTrue(login_page.is_url_login(), "Falha ao logar")

        login_page.exec_login()

        order_users_page.go_to_admin_page()
        self.assertTrue(order_users_page.is_user_on_admin_page(), "Falha ao navegar para a página")

        order_users_page.order_users_by_username_asc()
        print("Usuários em ordem ascedente")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
