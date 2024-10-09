from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_flipkart(self):
        self.driver.get("https://www.flipkart.com")

    def search_for_item(self, item_name):
        search_input = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")))
        search_input.send_keys(item_name)
        search_input.send_keys(Keys.DOWN)
        search_input.send_keys(Keys.ENTER)

    def get_item_text(self):
        item_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='KzDlHZ'])[1]")))
        return item_text.text

    def click_first_item(self):
        item_click = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='tUxRFH'])[1]")))
        item_click.click()

    def add_to_cart(self):
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add to cart']")))
        add_to_cart_button.click()

    def place_order(self):
        place_order_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Place Order']")))
        place_order_button.click()

    def enter_phone_number(self, phone_number):
        phone_no_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text']")))
        phone_no_text.send_keys(phone_number)

    def click_continue(self):
        continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        continue_button.click()

    def enter_otp(self):
        enter_otp = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@class='r4vIwl zgwPDa Jr-g+f']")))
        enter_otp.click()
        input("Please enter OTP manually and press Enter to continue...")
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()
