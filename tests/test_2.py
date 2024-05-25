
from pages.RecruitmentPage import RecruitmentPage


class TestCase2:

    def test_deletar_candidato(self, login_app):
        login_page, user_page = login_app
        user_page.open_side_menu_option('Recruitment')
        recruitment_page = RecruitmentPage(driver=login_page.driver)
        before, after = recruitment_page.delete_candidate()
        recruitment_page.was_candidate_deleted(before=before, after=after)