from pages.base_page import Page
from selenium.webdriver.common.by import By

class OffPlanPage(Page):
    OFF_PLAN_TITLE = (By.XPATH, '//button[text()="Off-plan"]')
    PRICE_BTN = (By.CSS_SELECTOR, '[data-test-id="filter-price-dropdown"]') # locates 1 visible and 1 invisible element
    FROM_BTN = (By.CSS_SELECTOR, '[data-test-id="price-min-input"]')
    TO_BTN = (By.CSS_SELECTOR, '[data-test-id="price-max-input"]')
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, 'button.inline-flex[type="submit"]')

    def verify_op_page_opened(self):
        self.wait_until_element_present(*self.OFF_PLAN_TITLE)
        self.find_element(*self.OFF_PLAN_TITLE)

    def filter_by_price_range(self):
        self.click_visible_element(*self.PRICE_BTN)
        self.wait_until_element_present(*self.FROM_BTN)
        self.input_text('1200000',*self.FROM_BTN)
        self.wait_until_element_present(*self.TO_BTN)
        self.input_text('2000000',*self.TO_BTN)
        self.wait_until_clickable_click(*self.APPLY_FILTER_BTN)

    def verify_price_range(self):
        self.verify_visible_element_text('1.2M - 2M AED',*self.PRICE_BTN)
