from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.post_login_Page import PostLoginPage
from pages.logoutPage import LogoutPage
from utils import utils
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login_page(self):
        driver = self.driver
        login = LoginPage(driver)
        print(driver.title)
        login.enter_email(utils.email)
        login.enter_password(utils.password)
        login.click_login_btn()

    def test_after_login_page(self):
        driver = self.driver
        postlogin = PostLoginPage(driver)
        postlogin.waiting_for_become_seller()
        postlogin.waiting_for_profile()
        postlogin.move_to_profile()

    def test_logout(self):
        try:
            driver = self.driver
            logout = LogoutPage(driver)
            logout.click_logout()
            logout.waiting_for_login_btn()
            logout.get_text_request_otp_btn()
            x = driver.title
            assert x == 'abc'

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            cur_time = moment.now().strftime("%d-%m-%Y_%H_%M_%S")
            testName = utils.whoami()
            # Above statement will return the function name
            screenshotName = testName + cur_time
            allure.attach(self.driver.get_screenshot_as_png(),
                          name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise
        except:
            print("Some exception occurred")
        else:
            print("No exceptions occurred")
        finally:
            print("This block will (lw(ys execute | Close DB")


