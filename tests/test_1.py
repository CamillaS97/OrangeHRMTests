import time

from pages.RecruitmentPage import RecruitmentPage


class TestCase1:
    first_name = 'Beetle'
    last_name = 'Juice'
    email = 'beetlejuice@email.com'

    def test_indicar_candidato(self, login_app):
        login_page, user_page = login_app
        user_page.open_side_menu_option('Recruitment')
        recruitment_page = RecruitmentPage(driver=login_page.driver)
        recruitment_page.open_add_candidate()
        recruitment_page.fill_recruitment_form(firstname=self.first_name, lastname=self.last_name, email=self.email)
        recruitment_page.submit_form()
        assert recruitment_page.is_application_stage_page()
        assert recruitment_page.is_form_correct(firstname=self.first_name, lastname=self.last_name, email=self.email)
