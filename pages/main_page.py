from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, '#email-2')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#field')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '.login-button.w-button')

    def open_main_page(self):
        self.open_url()
        # sleep(3) # enable when using Firefox

    def log_in_main_page(self):
        self.input_text('foriv86434@manupay.com', *self.EMAIL_FIELD)
        self.input_text('*', *self.PASSWORD_FIELD)
        self.wait_until_clickable_click(*self.CONTINUE_BUTTON)
