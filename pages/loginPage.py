from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.enter_email_by_xpath = '//input[@class="_2IX_2- VJZDxU"]'
        self.enter_password_by_xpath = '//input[@class="_2IX_2- _3mctLh VJZDxU"]'
        self.click_login_btn_by_xpath = "//button/span[text()='Login']"

    def enter_email(self, email):
        driver = self.driver
        driver.find_element(By.XPATH, self.enter_email_by_xpath).clear()
        driver.find_element(By.XPATH, self.enter_email_by_xpath).send_keys(email)

    def enter_password(self, password):
        driver = self.driver
        driver.find_element(By.XPATH, self.enter_password_by_xpath).clear()
        driver.find_element(By.XPATH, self.enter_password_by_xpath).send_keys(password)

    def click_login_btn(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.click_login_btn_by_xpath).click()
