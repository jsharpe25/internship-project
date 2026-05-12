from behave import when, then

@then('Verify the Agency page opens')
def step_verify_agency_page(context):
    context.app.settings_for_agency_page.verify_agency_page()

@when('Scroll to the "Contact us for details" form')
def step_scroll_to_form(context):
    context.app.settings_for_agency_page.scroll_to_form()

@then('Verify the "Contact us for details" form is available')
def step_verify_contact_us_form(context):
    context.app.settings_for_agency_page.verify_contact_us_form()
