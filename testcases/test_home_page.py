import pytest
from selenium import webdriver
from pages.home_page import HomePage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestHomePage:

    def test_home_page_elements(self):
        home_page = HomePage(self.driver)
        home_page.open_flipkart()

        # Verify the presence of the navigation menu
        assert home_page.is_navigation_menu_present(), "Navigation menu is not present on the homepage."

        # Verify the presence of the search bar
        assert home_page.is_search_bar_present(), "Search bar is not present on the homepage."

        # Verify the presence of the footer
        assert home_page.is_footer_present(), "Footer is not present on the homepage."

