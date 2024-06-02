from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class EditUserPage:
    def __init__(self, driver):
        self.driver = driver

    def open_edit_page(self):
        edit_user_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser/1"
        self.driver.get(edit_user_url)
        print("Opened edit page for user ID: 1")

    def edit_user_first_name(self, new_first_name):
        try:
            first_name_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input"))
            )
            first_name_field.clear()
            first_name_field.send_keys(new_first_name)

            save_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            save_button.click()

            print(f"Updated first name to: {new_first_name}")
        except TimeoutException:
            print("The first name field was not found.")
