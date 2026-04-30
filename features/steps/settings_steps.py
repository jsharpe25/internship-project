from behave import when, then

@when('Select "My clients" profile option')
def step_click_my_clients_btn(context):
    context.app.settings_page.click_my_clients_btn()

@when('Select "Dashboard"')
def step_click_dashboard_tab(context):
    context.app.settings_my_clients_page.click_dashboard_tab()

@then('Verify Dashboard page is opened')
def step_verify_dashboard_page(context):
    context.app.settings_my_clients_page.verify_dashboard_page()

@then('Verify the referral link contains "https://soft.reelly.io/sign-up"')
def step_verify_referral_link(context):
    context.app.settings_my_clients_page.verify_referral_link()
