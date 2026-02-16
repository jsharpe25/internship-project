from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """

    context.driver = webdriver.Chrome()

    # Firefox and Safari
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Safari()

    # Headless Mode
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(
    #     options=options
    # )

    context.driver.implicitly_wait(4) # disable when using Firefox
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.driver.maximize_window()
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
