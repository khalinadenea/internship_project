from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class settings(Page):
    USER_GUIDE_LINK = (By.LINK_TEXT, "User guide")

    def click_user_guide(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.USER_GUIDE_LINK)
        )
        # Scroll into view just in case
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
