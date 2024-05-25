
from pages.PIMPage import PIMPage


class TestCase3:
    first_name = 'Beetle'
    last_name = 'Juice'
    pass_word = 'Senha123'
    user_name = 'beetlejuice'

    def test_criar_perfil(self, login_app):
        login_page, user_page = login_app
        user_page.open_side_menu_option('PIM')
        pim_page = PIMPage(driver=login_page.driver)
        pim_page.add_employee(firstname=self.first_name, lastname=self.last_name, password=self.pass_word, username=self.user_name)
        assert pim_page.employee_was_created(firstname=self.first_name, lastname=self.last_name)
