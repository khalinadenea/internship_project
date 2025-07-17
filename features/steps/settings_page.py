from behave import when


@when('the user clicks on the User Guide option')
def open_user_guide(context):
    context.app.settings_page.click_user_guide()
