from pages.main_page import MainPage
from pages.sign_in_page import SignIn
from pages.reelly_homepage import homepage
from pages.settings_page import settings
from pages.user_guide_page import UserGuide


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.sign_in_page = SignIn(driver)
        self.reelly_homepage = homepage(driver)
        self.settings_page = settings(driver)
        self.user_guide_page = UserGuide(driver)
