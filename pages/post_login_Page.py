from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PostLoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait_visibility_of_element_located_become_seller = '//span[text()="Become a Seller"]'
        self.wait_visibility_of_element_located_profile = '//div[text()="Raj"]'
        self.move_to = '//div[text()="Raj"]'

    def waiting_for_become_seller(self):
        driver = self.driver
        wait = WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.wait_visibility_of_element_located_become_seller)))

    def waiting_for_profile(self):
        driver = self.driver
        wait = WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.wait_visibility_of_element_located_profile)))

    def move_to_profile(self):
        driver = self.driver
        a = ActionChains(driver)
        m = driver.find_element(By.XPATH, self.move_to)
        a.move_to_element(m).perform()
