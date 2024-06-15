
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.PageObject import PageObject


class UserPage(PageObject):
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    header = (By.CLASS_NAME, 'oxd-topbar-header-title')
    search_field = (By.CSS_SELECTOR, "[placeholder='Search']")

    def __init__(self, driver):
        super(UserPage, self).__init__(driver=driver)

    def open_side_menu_option(self, option='Dashboard'):
        self.driver.find_element(By.LINK_TEXT, option).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.header, option))

    def open_side_menu_option_my_info(self, option='Dashboard'):
        self.driver.find_element(By.LINK_TEXT, option).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.header, 'PIM'))

    def is_dashboard_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.header))
        return self.driver.find_element(*self.header).text == 'Dashboard'

    def open_side_menu_search(self, option):
        self.driver.find_element(*self.search_field).send_keys(option)

    def is_menu_option_present(self, option):
        return self.driver.find_element(By.LINK_TEXT, option).is_displayed()
