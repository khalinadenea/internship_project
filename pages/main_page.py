from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class MainPage(Page):

    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '[wized="signinButtonSignup"]')

    def open_main_page(self):
        self.driver.get('https://soft.reelly.io/sign-up')
        sleep(10)

    def click_sign_in(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
        ).click()
