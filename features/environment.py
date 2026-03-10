import os

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application

load_dotenv()


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # Chrome
    options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    context.driver = webdriver.Chrome(options=options)
    context.is_mobile = False

    # Firefox
    # context.driver = webdriver.Firefox()
    # context.is_mobile = False

    # Browserstack Web
    # bs_user = os.getenv("BROWSERSTACK_USERNAME")
    # bs_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
    # if not bs_user or not bs_key:
    #     raise Exception("BrowserStack credentials not set in .env file.")
    # client_config = ClientConfig(remote_server_addr="https://hub-cloud.browserstack.com/wd/hub", username=bs_user, password=bs_key)
    # remote_connection = RemoteConnection(client_config=client_config)
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Tahoe',
    #     'browserName': 'Safari',
    #     'browserVersion': 'latest',
    #     "projectName": "Price Range Filter",
    #     "buildName": "reelly_v2.6",
    #     'sessionName': scenario_name
    # }
    # options = Options()
    # options.set_capability('bstack:options', bstack_options)
    # prefs = {"profile.default_content_setting_values.notifications": 2}
    # options.add_experimental_option("prefs", prefs)
    # context.driver = webdriver.Remote(command_executor=remote_connection, options=options)
    # context.is_mobile = False

    # Browserstack Mobile
    # bs_user = os.getenv("BROWSERSTACK_USERNAME")
    # bs_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
    # if not bs_user or not bs_key:
    #     raise Exception("BrowserStack credentials not set in .env file.")
    # client_config = ClientConfig(remote_server_addr="https://hub-cloud.browserstack.com/wd/hub", username=bs_user, password=bs_key)
    # remote_connection = RemoteConnection(client_config=client_config)
    # bstack_options = {
    #     'deviceName' : 'Samsung Galaxy S22 Ultra',
    #     'osVersion': '12.0',
    #     'browserName': 'Chrome',
    #     'projectName': 'Price Range Filter',
    #     'buildName': 'reelly_v2.6',
    #     'sessionName': scenario_name,
    # }
    # options = Options()
    # options.set_capability('bstack:options', bstack_options)
    # options.add_argument('--disable-notifications')
    # context.driver = webdriver.Remote(command_executor=remote_connection, options=options)
    # context.is_mobile = True

    # Mobile Emulation
    # mobile_emulation = {"deviceName": "Samsung Galaxy S8+"}
    # options = Options()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # prefs = {"profile.default_content_setting_values.notifications": 2}
    # options.add_experimental_option("prefs", prefs)
    # context.driver = webdriver.Chrome(options=options)
    # context.is_mobile = True

    # Headless Mode
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(options=options)
    # context.is_mobile = False

    context.browser_name = context.driver.capabilities.get("browserName", "").lower()
    context.is_firefox = context.browser_name == "firefox"
    if context.is_firefox:
        context.driver.implicitly_wait(0)
    else:
        context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    if not context.is_mobile:
        context.driver.maximize_window()
    context.app = Application(context.driver, context.is_mobile)


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
