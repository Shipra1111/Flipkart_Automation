from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_url(self):
        self.driver.get("https://www.flipkart.com")

    def open_login_page(self):
       click_login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Login']")))
       click_login_button.click()

    def enter_mobile(self, mobile_number):
        mobile_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='r4vIwl BV+Dqf']")))
        mobile_input.send_keys(mobile_number)

    def click_request_otp(self):
        request_otp = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Request OTP']")))
        request_otp.click()

    def enter_otp(self, otp):
        otp_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='XDRRi5']")))
        otp_input.send_keys(otp)

    def click_verify(self):
        verify_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Verify']")))
        verify_button.click()

    def click_account_button(self):
        verify_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Account']")))
        verify_button.click()

    def get_error_message(self):
        error_message_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Please enter valid Email ID/Mobile number')]")))
        return error_message_element.text

    def logout(self):
        logout_button = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//li[8]")))
        logout_button.click()