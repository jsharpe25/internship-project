from behave import given


@given('Open the main page')
def step_open_main_page(context):
    context.app.main_page.open_main_page()


@given('Log in to the page')
def step_log_in_main_page(context):
    context.app.main_page.log_in_main_page()
