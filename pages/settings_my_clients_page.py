from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsMyClientsPage(Page):
    DASHBOARD_TAB = (By.XPATH, '//a[text()="Dashboard"]')
    DASHBOARD_TITLE = (By.XPATH, '//div[text()="Dashboard"]')
    REFERRAL_LINK = (By.CSS_SELECTOR, '.private-block-leaderboard .text-field.w-input')

    def select_dashboard(self):
        self.wait_until_clickable_click(*self.DASHBOARD_TAB)

    def verify_dashboard_page(self):
        self.wait_until_element_visible(*self.DASHBOARD_TITLE)
        self.verify_text('Dashboard', *self.DASHBOARD_TITLE)

    def verify_referral_link(self):
        self.wait_until_element_visible(*self.REFERRAL_LINK)
        self.verify_input_value_contains('https://soft.reelly.io/sign-up', *self.REFERRAL_LINK)
