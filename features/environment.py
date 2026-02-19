from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

load_dotenv()


def browser_init(context, scenario_name):
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


    # Browserstack
    # bs_user = 'joelsharpe_olgqZL'
    # bs_key = 'q9LStYCbGxqeG6s2gTjg'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Tahoe',
    #     'browserVersion': 'latest',
    #     'browserName': 'Safari',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.implicitly_wait(4) # disable while using Firefox
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.driver.maximize_window()
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
