from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject

class LoginPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    username_field = (By.CSS_SELECTOR, '[name="username"]')
    password_field = (By.CSS_SELECTOR, '[name="password"]')
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)

    def __init__(self, driver=None, browser=None):
        super(LoginPage, self).__init__(driver, browser)

    def open_login_page(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_field))

    def is_url_login(self):
        return self.is_url(self.url)

    def click_login_button(self):
        self.driver.find_element(*self.login_btn).click()

    def exec_login(self, username='Admin',password='admin123'):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.click_login_button()
