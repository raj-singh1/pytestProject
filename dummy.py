from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(
            executable_path="C:/Users/raj_r/PycharmProjects/pytestProject/drivers/chromedriver.exe")
        driver.get("https://www.flipkart.com/")
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Sample Run Completed")

    def test_login_page(self, test_setup):
        print(driver.title)
        driver.find_element(By.XPATH, '//input[@class="_2IX_2- VJZDxU"]').clear()
        driver.find_element(By.XPATH, '//input[@class="_2IX_2- VJZDxU"]').send_keys("8097881727")
        driver.find_element(By.XPATH, '//input[@class="_2IX_2- _3mctLh VJZDxU"]').clear()
        driver.find_element(By.XPATH, '//input[@class="_2IX_2- _3mctLh VJZDxU"]').send_keys("Quark@123")
        driver.find_element(By.XPATH, "//button/span[text()='Login']").click()

    def test_after_login_page(self, test_setup):
        wait = WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Become a Seller"]')))
        wait = WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Raj"]')))
        a = ActionChains(driver)
        m = driver.find_element(By.XPATH, '//div[text()="Raj"]')
        a.move_to_element(m).perform()

    def test_logout(self, test_setup):
        driver.find_element(By.XPATH, '//div[text()="Logout"]').click()
        wait = WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))
        print(driver.find_element(By.XPATH, "//button[text()='Request OTP']").text)