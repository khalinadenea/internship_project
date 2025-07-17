from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignIn(Page):
    USERNAME_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_FIELD = (By.CSS_SELECTOR, '.login-button')

    username = 'khalinaboyce@gmail.com'
    password = 'Dionneb131!'

    def input_username(self):
        self.input_text(self.username, *self.USERNAME_FIELD)

    def input_password(self):
        self.input_text(self.password, *self.PASSWORD_FIELD)

    def click_continue(self):
        self.click(*self.CONTINUE_FIELD)
