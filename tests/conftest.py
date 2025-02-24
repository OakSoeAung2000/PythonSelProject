import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )





@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif browser_name == "firefox":
        print("Firefox")
        #firefox browser invocation
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()