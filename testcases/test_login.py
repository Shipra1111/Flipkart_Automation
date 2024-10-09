import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_url()
        login_page.open_login_page()
        login_page.enter_mobile("9650086624")  # Replace with a valid mobile number
        login_page.click_request_otp()
        input("Enter the OTP sent to your mobile: ")
        login_page.click_verify()
        login_page.click_account_button()
        login_page.logout()
        # Add assertions to verify successful login

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_url()
        login_page.open_login_page()
        login_page.enter_mobile("12345")  # Replace with an invalid mobile number
        login_page.click_request_otp()
        error_message = login_page.get_error_message()
        assert error_message == "Please enter a valid mobile number", "Error message did not match."
