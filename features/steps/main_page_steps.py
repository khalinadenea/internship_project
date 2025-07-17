from behave import given
from time import sleep


@given('the user navigates to the main page')
def open_main(context):
    sleep(10)
    context.app.main_page.open_main_page()


@given('the user clicks on the sign in button')
def click_sign_in_btn(context):
    context.app.main_page.click_sign_in()
