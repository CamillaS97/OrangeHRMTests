from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageObject import PageObject

class SearchUsuarioPage(PageObject):
    admin_menu = (By.CSS_SELECTOR, "a[href='/web/index.php/admin/viewAdminModule']")
    admin_page_header = (By.XPATH, "//h6[text()='Admin']")
    search_username_input = (By.XPATH, "//label[text()='Username']/following::input[1]")
    search_button = (By.XPATH, "//button[@type='submit']")
    result_username = (By.XPATH, "//div[@role='row']//div[contains(text(),'Admin')]")

    def __init__(self, driver=None, browser=None):
        super(SearchUsuarioPage, self).__init__(driver, browser)

    def go_to_admin_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.admin_menu)
        ).click()

    def is_user_on_admin_page(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.admin_page_header)
            )
            return True
        except:
            return False

    def search_user(self, username):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_username_input)
        )
        search_input.clear()
        search_input.send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

    def is_user_found(self, username):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//div[@role='row']//div[contains(text(),'{username}')]"))
            )
            return True
        except:
            return False
