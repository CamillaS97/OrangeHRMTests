from pages.PageObject import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RecruitmentPage(PageObject):
    add_btn = (By.XPATH, '//*[@class="oxd-button oxd-button--medium oxd-button--secondary"]')
    candidate_form_header = (By.XPATH, '//*[@class="orangehrm-card-container"]/h6')
    first_name_field = (By.NAME, 'firstName')
    last_name_field = (By.NAME, 'lastName')
    save_btn = (By.CSS_SELECTOR, "button[type='submit']")
    email_field = (By.XPATH, '//*[@id="app"]//div[3]//div[1]/div/div[2]/input')
    main_title_field = (By.XPATH, '//*[@class="orangehrm-card-container"]/form/h6')
    default_firstname = 'John'
    default_lastname = 'Doe'
    default_email = 'johndoe@email.com'

    def __init__(self, driver):
        super(RecruitmentPage, self).__init__(driver=driver)

    def open_add_candidate(self):
        self.driver.find_element(*self.add_btn).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.candidate_form_header))
        assert self.driver.find_element(*self.candidate_form_header).text == "Add Candidate"

    def fill_recruitment_form(self, firstname=default_firstname, lastname=default_lastname, email=default_email):
        self.driver.find_element(*self.first_name_field).send_keys(firstname)
        self.driver.find_element(*self.last_name_field).send_keys(lastname)
        self.driver.find_element(*self.email_field).send_keys(email)

    def submit_form(self):
        self.driver.find_element(*self.save_btn).click()

    def is_application_stage_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.main_title_field))
        return self.driver.find_element(*self.main_title_field).text == "Application Stage"

    def is_form_correct(self, firstname=default_firstname, lastname=default_lastname, email=default_email):
        first_name_correct = self.driver.find_element(*self.first_name_field).get_attribute('value') == firstname
        last_name_correct = self.driver.find_element(*self.last_name_field).get_attribute('value') == lastname
        email_correct = self.driver.find_element(*self.email_field).get_attribute('value') == email

        return first_name_correct and last_name_correct and email_correct
