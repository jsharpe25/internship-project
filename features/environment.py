from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.client_config import ClientConfig
import os
from dotenv import load_dotenv
from app.application import Application

load_dotenv()


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # Chrome
    context.driver = webdriver.Chrome()

    # Firefox and Safari
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Safari()

    # Browserstack
    # bs_user = os.getenv("BROWSERSTACK_USERNAME")
    # bs_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
    # if not bs_user or not bs_key:
    #     raise Exception("BrowserStack credentials not set in .env file.")
    # client_config = ClientConfig(
    #     remote_server_addr="https://hub-cloud.browserstack.com/wd/hub",
    #     username=bs_user,
    #     password=bs_key
    # )
    # remote_connection = RemoteConnection(client_config=client_config)
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Tahoe',
    #     'browserVersion': 'latest',
    #     'browserName': 'Safari',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=remote_connection, options=options)

    # Headless Mode
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(options=options)

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
    if hasattr(context, "driver"):
        context.driver.quit()
