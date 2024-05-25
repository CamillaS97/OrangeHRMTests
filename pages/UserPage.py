from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class UserPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    header = (By.CLASS_NAME, 'oxd-topbar-header-title')

    def __init__(self, driver):
        super(UserPage, self).__init__(driver=driver)

    def open_side_menu_option(self, option='Dashboard'):
        self.driver.find_element(By.LINK_TEXT, option).click()

    def is_dashboard_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.header))
        return self.driver.find_element(*self.header).text == 'Dashboard'
