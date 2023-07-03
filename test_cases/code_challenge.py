from selenium import webdriver
from page_objects.GoogleSearch import GoogleSearch
from selenium.webdriver.common.by import By


class TestE2E:

    driver = webdriver.Chrome()
    driver.get("https://www.google.com/search?q=1")

    def test_e2e(self):

        print("\nTest Running*************")
        input_search = "Juan"

        self.e2e = GoogleSearch(self.driver)
        assert(self.e2e.if_exist_g_logo())
        self.driver.implicitly_wait(10)
        assert(self.e2e.input_search_g_textarea(input_search))
        self.driver.implicitly_wait(10)
        self.e2e.click_search()
        self.driver.implicitly_wait(30)
        assert(self.e2e.validate_search(input_search))
