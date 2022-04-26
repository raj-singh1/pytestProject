from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    def __init__(self ,driver):
        self.driver = driver
        self.click_logout_by_xpath = '//div[text()="Logout"]'
        self.wait_for_login_btn_by_xpath = "//button/span[text()='Login']"
        self.get_text_request_otp_btn_by_xpath = "//button[text()='Request OTP']"

    def click_logout(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.click_logout_by_xpath).click()

    def waiting_for_login_btn(self):
        driver = self.driver
        wait = WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))

    def get_text_request_otp_btn(self):
        driver = self.driver
        print(driver.find_element(By.XPATH, self.get_text_request_otp_btn_by_xpath).text)