import random
import time

from selenium.webdriver import Keys

from pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage(PageObject):
    add_btn = (By.XPATH, '//button[text()=" Add "]')
    employee_form_header = (By.XPATH, '//*[@class="orangehrm-card-container"]/h6')
    login_details_btn = (By.XPATH, '//*[@id="app"]//div[2]/div/label')
    first_name_field = (By.NAME, 'firstName')
    last_name_field = (By.NAME, 'lastName')
    employee_id_field = (By.XPATH, '//*[@id="app"]//div[2]/div/div/div[2]/input')
    username_field = (By.XPATH, '//*[@id="app"]//div[3]/div/div[1]/div/div[2]/input')
    password_field = (By.CSS_SELECTOR, 'input[type=password]')
    save_btn = (By.CSS_SELECTOR, "button[type='submit']")
    personal_detail_title = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6')
    employee_name_field = (By.CLASS_NAME, 'orangehrm-edit-employee-name')
    default_firstname = 'Bruce'
    default_lastname = 'Wayne'
    default_username = 'batman'
    default_password = 'Senha123'

    def __init__(self, driver):
        super(PIMPage, self).__init__(driver=driver)

    def open_add_employee(self):
        self.driver.find_element(*self.add_btn).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.employee_form_header))
        assert self.driver.find_element(*self.employee_form_header).text == "Add Employee"

    def create_login_details(self):
        self.driver.find_element(*self.login_details_btn).click()
        assert self.driver.find_element(*self.username_field).is_displayed()

    # Funcao clear nao funciona para esse campo, tive que usar CONTROL+a e Del
    def fill_employee_form(self, firstname=default_firstname, lastname=default_lastname,username=default_username, password=default_password):
        self.driver.find_element(*self.first_name_field).send_keys(firstname)
        self.driver.find_element(*self.last_name_field).send_keys(lastname)
        self.driver.find_element(*self.employee_id_field).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.driver.find_element(*self.employee_id_field).send_keys(str(random.randint(0, 500)))
        self.driver.find_element(*self.username_field).send_keys(username + str(random.randint(0, 200)))
        pwd = self.driver.find_elements(*self.password_field)
        pwd[0].send_keys(password)
        pwd[1].send_keys(password)

    def submit_form(self):
        self.driver.find_element(*self.save_btn).click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(self.personal_detail_title, 'Personal Details'))
        assert self.driver.find_element(*self.personal_detail_title).text == "Personal Details"

    def employee_was_created(self, firstname=default_firstname, lastname=default_lastname):
        complete_name = firstname + " " + lastname
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(self.employee_name_field, complete_name))
        return self.driver.find_element(*self.employee_name_field).text == complete_name

    def add_employee(self, firstname=default_firstname, lastname=default_lastname, username=default_username, password=default_password):
        self.open_add_employee()
        self.create_login_details()
        self.fill_employee_form(firstname=firstname, lastname=lastname, username=username, password=password)
        self.submit_form()
