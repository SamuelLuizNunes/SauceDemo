from selenium import webdriver
from selenium.webdriver.common.by import By
class TestProdutos():
    url = 'https://www.saucedemo.com'


    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_selecionar_produto(self):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')