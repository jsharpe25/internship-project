from behave import when, then

@then('Verify the University page opens')
def step_verify_university_page(context):
    context.app.university_page.verify_university_page()

@when('Click on the “Calendar” option')
def step_click_calendar_option(context):
    context.app.university_page.click_calendar_option()

@when('Click on the “Bali Course” option')
def step_click_bali_option(context):
    context.app.university_page.click_bali_option()

@then('Verify "Bali Course Lessons", "Q/A sessions", and "Discover last podcast" content headers and media cards')
def step_verify_content_headers_and_cards(context):
    context.app.university_page.verify_content_headers_and_cards()
