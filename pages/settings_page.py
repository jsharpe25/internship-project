from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsPage(Page):
    MY_CLIENT_BTN = (By.XPATH, '//div[text()="My clients"]')
    FOR_AGENCY_BTN = (By.XPATH, '//div[text()="For agency"]')

    def select_my_clients(self):
        self.wait_until_clickable_click(*self.MY_CLIENT_BTN)

    def select_for_agency(self):
        self.wait_until_clickable_click(*self.FOR_AGENCY_BTN)
