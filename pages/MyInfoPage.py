import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

from pages.PageObject import PageObject


class MyInfoPage(PageObject):
    save_button = (By.XPATH, "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//form//button[@type='submit']")
    # first_name_field = (By.CSS_SELECTOR, "[placeholder='First Name']")
    first_name_field = (By.CLASS_NAME, 'orangehrm-firstname')
    last_name_field = (By.CLASS_NAME, 'orangehrm-lastname')

    def __init__(self, driver):
        super(MyInfoPage, self).__init__(driver=driver)

    def edit_employee_name(self, first_name, last_name):
        for x in range(1, 30):
            self.driver.find_element(*self.first_name_field).send_keys(Keys.BACKSPACE)
        for x in range(1, 30):
            self.driver.find_element(*self.last_name_field).send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()

    def is_name_title_found(self, username):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//p[@class='oxd-userdropdown-name'][text()='{username}']"))
            )
            return True
        except:
            return False

