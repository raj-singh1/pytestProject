import pytest

from utils import utils


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")
#     Function use to pass value or parameter at runtime


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(
            executable_path="C:/Users/raj_r/PycharmProjects/pytestProject/drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path="C:/Users/raj_r/PycharmProjects/pytestProject/drivers/geckodriver.exe")
    driver.get(utils.url)
    driver.maximize_window()
    request.cls.driver = driver
    # Above line is use of pass driver instance to class TestLogin
    yield
    driver.close()
    driver.quit()
