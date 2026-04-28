from pages.base_page import Page
from selenium.webdriver.common.by import By

class SidebarPage(Page):
    OFF_PLAN_BTN = (By.CSS_SELECTOR, '[aria-label="Off-plan"]')
    SETTINGS_BTN = (By.CSS_SELECTOR, '[aria-label="Settings"]')

    def click_off_plan_btn(self):
        self.wait_until_clickable_click(*self.OFF_PLAN_BTN)

    def click_settings_btn(self):
        self.wait_until_clickable_click(*self.SETTINGS_BTN)
