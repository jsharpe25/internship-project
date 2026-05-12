from behave import when, then

@when('Select "Dashboard"')
def step_select_dashboard(context):
    context.app.settings_my_clients_page.select_dashboard()

@then('Verify Dashboard page is opened')
def step_verify_dashboard_page(context):
    context.app.settings_my_clients_page.verify_dashboard_page()

@then('Verify the referral link contains "https://soft.reelly.io/sign-up"')
def step_verify_referral_link(context):
    context.app.settings_my_clients_page.verify_referral_link()
