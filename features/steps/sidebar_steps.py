from behave import when


@when('Select “Off-plan” in the sidebar')
def step_select_off_plan(context):
    context.app.sidebar_page.select_off_plan()

@when('Select profile in the sidebar')
def step_select_profile(context):
    context.app.sidebar_page.select_profile()
