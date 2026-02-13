from behave import when


@when('Click on “Off-plan” in the left side menu')
def step_click_off_plan_tab(context):
    context.app.side_menu_page.click_off_plan_tab()

