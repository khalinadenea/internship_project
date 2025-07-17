from behave import then


@then('the User Guide page should open with the lesson video title visible')
def verify_user_guide_ui_elements(context):
    assert context.app.user_guide_page.is_video_visible(), "Video is not visible"
    assert context.app.user_guide_page.is_video_title_correct(), "Video title is incorrect or missing"

