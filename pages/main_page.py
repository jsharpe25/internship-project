from pages.base_page import Page
from selenium.webdriver.common.by import By
import os
from time import sleep


class MainPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, '#email-2')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#field')
    CONTINUE_BTN = (By.CSS_SELECTOR, '.login-button.w-button')

    def _maybe_slow_down(self): # Sleep for a few seconds only on Firefox or Safari
        browser = self.driver.capabilities.get('browserName', '').lower()
        if browser in ('firefox', 'safari'):
            sleep(3)

    def open_main_page(self):
        self.open_url()
        self._maybe_slow_down()

    def log_in_main_page(self):
        email = os.getenv("TEST_EMAIL")
        password = os.getenv("TEST_PASSWORD")
        self.input_text(email, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.remove_focus()
        self.wait_until_clickable_click(*self.CONTINUE_BTN)
        self._maybe_slow_down()
