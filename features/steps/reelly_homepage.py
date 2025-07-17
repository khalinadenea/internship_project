from behave import when


@when('the user clicks on the settings option')
def click_on_settings(context):
    context.app.reelly_homepage.click_settings()
