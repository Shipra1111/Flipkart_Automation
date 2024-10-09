from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_flipkart(self):
        self.driver.get("https://www.flipkart.com")

    def is_search_bar_present(self):
        try:
            # Wait for the search bar to be visible and return if it is displayed
            search_bar = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")))
            return search_bar.is_displayed()
        except:
            return False

    def is_navigation_menu_present(self):
        try:
            # Update the XPath to the correct one
            navigation_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='_3sdu8W emupdz']")))
            return navigation_menu.is_displayed()
        except Exception:
            return False

    def scroll_to_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_footer_present(self):
        self.scroll_to_footer()
        footer = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//footer")))
        return footer.is_displayed()

