from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsPage(Page):
    MY_CLIENT_BTN = (By.XPATH, '//div[text()="My clients"]')

    def click_my_clients_btn(self):
        self.wait_until_clickable_click(*self.MY_CLIENT_BTN)
