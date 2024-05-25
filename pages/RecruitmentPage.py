
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
    candidate_qty_field = (By.XPATH, '//*[@id="app"]//div[2]/div/span')
    delete_selected_btn = (By.XPATH, '//button[text()=" Delete Selected "]')
    yes_delete_btn = (By.XPATH, '//button[text()=" Yes, Delete "]')
    delete_popup_title = (By.XPATH, '//p[text()="Are you Sure?"]')
    default_firstname = 'John'
    default_lastname = 'Doe'
    default_email = 'johndoe@email.com'
    table_class = (By.CLASS_NAME, 'oxd-table-card')
    checkbox_btn = (By.TAG_NAME, "input")

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

    def select_first_candidate(self):
        complete_table = self.driver.find_elements(*self.table_class)
        first_element = complete_table[0]
        first_checkbox = first_element.find_element(*self.checkbox_btn)
        self.driver.execute_script("arguments[0].click();", first_checkbox)
        assert self.driver.find_element(*self.delete_selected_btn).is_displayed()

    def click_delete_button(self):
        self.driver.find_element(*self.delete_selected_btn).click()
        assert self.driver.find_element(*self.delete_popup_title).is_displayed()

    def confirm_delete_popup(self):
        self.driver.find_element(*self.yes_delete_btn).click()

    def get_candidate_qty(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.candidate_qty_field))
        qty = self.driver.find_element(*self.candidate_qty_field).text
        qty = qty.replace('(', '')
        qty = qty.replace(') Records Found', '')
        return int(qty)

    def delete_candidate(self):
        before = self.get_candidate_qty()
        self.select_first_candidate()
        self.click_delete_button()
        self.confirm_delete_popup()
        after = self.get_candidate_qty()
        return before, after

    def was_candidate_deleted(self, after=0, before=0):
        return after == before - 1
