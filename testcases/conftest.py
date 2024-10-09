from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.flipkart.com")
    request.cls.driver = driver
    yield
    driver.close()
