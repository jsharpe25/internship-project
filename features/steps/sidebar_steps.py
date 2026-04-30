from behave import when


@when('Select “Off-plan” in the sidebar')
def step_click_off_plan_btn(context):
    context.app.sidebar_page.click_off_plan_btn()

@when('Select "Settings" in the sidebar')
def step_click_settings_btn(context):
    context.app.sidebar_page.click_settings_btn()
