from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class OrderUsersPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_admin_page(self):
        admin_page_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        self.driver.get(admin_page_url)

    def is_user_on_admin_page(self):
        return "viewSystemUsers" in self.driver.current_url

    def order_users_by_username_asc(self):
        try:
            username_sort_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[2]/div/i"))
            )
            username_sort_icon.click()

            # Aguardar a atualização da página após a ordenação
            WebDriverWait(self.driver, 10).until(
                EC.staleness_of(username_sort_icon)
            )
            print("Uusários em ordem ascedente.")
        except TimeoutException:
            print("O ícone de classificação do nome de usuário não foi encontrado ou clicável")
