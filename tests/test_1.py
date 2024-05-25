
from pages.RecruitmentPage import RecruitmentPage


class TestCase1:
    first_name = 'Beetle'
    last_name = 'Juice'
    email = 'beetlejuice@email.com'

    def test_indicar_candidato(self, login_app):
        login_page, user_page = login_app
        user_page.open_side_menu_option('Recruitment')
        recruitment_page = RecruitmentPage(driver=login_page.driver)
        recruitment_page.add_candidate(firstname=self.first_name, lastname=self.last_name, email=self.email)
        assert recruitment_page.is_application_stage_page()
        assert recruitment_page.is_form_correct(firstname=self.first_name, lastname=self.last_name, email=self.email)
