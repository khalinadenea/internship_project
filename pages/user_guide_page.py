from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserGuide(Page):
    VIDEO_IFRAME = (By.CSS_SELECTOR, "iframe[src*='youtube.com']")
    VIDEO_TITLE = (By.CLASS_NAME, "next-event-text")

    def is_video_visible(self):
        iframe = self.wait.until(
            EC.presence_of_element_located(self.VIDEO_IFRAME)
        )
        return iframe.is_displayed()

    def is_video_title_correct(self, expected_title="User guide"):
        title_element = self.wait.until(
            EC.visibility_of_element_located(self.VIDEO_TITLE)
        )
        return expected_title.lower() in title_element.text.lower()
