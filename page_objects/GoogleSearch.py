from selenium.webdriver.common.by import By


class GoogleSearch:

    google_textbox_css = "#logo img"
    google_textarea_css = "textarea#APjFqb"
    google_button_search_css = ".Tg7LZd"

    def __init__(self, driver):
        self.driver = driver

    def if_exist_g_logo(self):
        """
        This method check if Google logo image exist
        :return:
        """
        g_logo_css = self.driver.find_element(By.CSS_SELECTOR, self.google_textbox_css)
        if g_logo_css.is_displayed():
            print("Locator 'Google logo' by CSS exists")
            return True
        else:
            print("Locator 'Google logo' logo by CSS doesn't exist")
            return False

    def input_search_g_textarea(self, input_value):
        """
        This method check if Google textarea exists and input a search text
        :param input_value: string to be search
        :return:
        """
        g_textbox_css = self.driver.find_element(By.CSS_SELECTOR, self.google_textarea_css)
        if g_textbox_css.is_displayed():
            print("Locator 'Google Search Textbox' by CSS exists")
            g_textbox_css.clear()
            g_textbox_css.send_keys(input_value)
            print(f"Google Search Textbox input {input_value} by CSS exists")
            return True
        else:
            print("Locator 'Google Search Textbox' by CSS doesn't exist")
            return False

    def click_search(self):
        """
        This method click on the Search button
        :return:
        """
        g_search_css = self.driver.find_element(By.CSS_SELECTOR, self.google_button_search_css)
        if g_search_css.is_displayed():
            print("Locator 'Search button' by CSS exists")
            g_search_css.click()
            print("Locator 'Search button' click")
            return True
        else:
            print("Locator 'Search button' by CSS doesn't exist")
            return False

    def validate_search(self, input_search):
        cssValue = self.driver.find_element(By.CSS_SELECTOR, self.google_textarea_css)
        text_search = cssValue.text
        if input_search == text_search:
            print(f"Text Search successfully: {text_search}")
            return True
        else:
            print(f"Text Search NOT successfully: {text_search}")
            return False

