import pytest
from selenium import webdriver
from pages.search_page import SearchPage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestSearchFunctionality:

    def test_search_page(self):
        search_page = SearchPage(self.driver)

        search_page.open_flipkart()
        search_page.search_for_item("iphone 15")

        # Capture the item text
       # captured_text = search_page.get_item_text()
       # print(f"Captured Item Text: {captured_text}")

        search_page.click_first_item()
        search_page.add_to_cart()
        search_page.place_order()

        search_page.enter_phone_number("9650086624")
        search_page.click_continue()
        search_page.enter_otp()
