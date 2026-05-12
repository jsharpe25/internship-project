from behave import when

@when('Select "My clients" profile option')
def step_select_my_clients(context):
    context.app.settings_page.select_my_clients()

@when('Select "For agency" profile option')
def step_select_for_agency(context):
    context.app.settings_page.select_for_agency()
