from behave import when


@when("the user logs in with valid credentials")
def valid_login(context):
    context.app.sign_in_page.input_username()
    context.app.sign_in_page.input_password()
    context.app.sign_in_page.click_continue()
