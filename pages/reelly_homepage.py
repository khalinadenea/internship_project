from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class homepage(Page):
    SETTINGS_BUTTON = (By.LINK_TEXT, "Settings")

    def click_settings(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SETTINGS_BUTTON)
        ).click()
