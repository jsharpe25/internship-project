from pages.base_page import Page
from selenium.webdriver.common.by import By

class SidebarPage(Page):
    OFF_PLAN_BTN = (By.CSS_SELECTOR, '[aria-label="Off-plan"]')
    PROFILE_BTN = (By.CSS_SELECTOR, 'a[href*="/settings"]')
    UNIVERSITY_BTN = (By.CSS_SELECTOR, '[aria-label="University"]')

    def select_off_plan(self):
        self.wait_until_clickable_click(*self.OFF_PLAN_BTN)

    def select_profile(self):
        self.wait_until_clickable_click(*self.PROFILE_BTN)

    def select_university(self):
        self.wait_until_clickable_click(*self.UNIVERSITY_BTN)
