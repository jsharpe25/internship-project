from behave import when, then


@when('Verify Off-plan page opened')
def step_verify_op_page_opened(context):
    context.app.off_plan_page.verify_op_page_opened()


@when('Filter the products by price range from 1200000 to 2000000 AED')
def step_filter_by_price_range(context):
    context.app.off_plan_page.filter_by_price_range()

@then('Verify the price in all cards is inside the range (1200000 - 2000000)')
def step_verify_price_range(context):
    context.app.off_plan_page.verify_price_range()
