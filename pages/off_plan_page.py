from pages.base_page import Page
from selenium.webdriver.common.by import By

class OffPlanPage(Page):
    DEVELOPER_BTN = {
        "mobile": (By.CSS_SELECTOR, '[class*="scrollbar-hide w-full"] [data-test-id="filter-developer-dropdown"]'),
        "web": (By.CSS_SELECTOR, '[class*="scrollbar-hide select-none"] [data-test-id="filter-developer-dropdown"]')
    }
    AARK_DEVELOPER_BTN = (By.CSS_SELECTOR, '[role="option"][data-value="Aark Developers"]')
    PRICE_BTN = {
        "mobile": (By.CSS_SELECTOR, '[class*="scrollbar-hide w-full"] [data-test-id="filter-price-dropdown"]'),
        "web": (By.CSS_SELECTOR, '[class*="scrollbar-hide select-none"] [data-test-id="filter-price-dropdown"]')
    }
    FROM_BTN = (By.CSS_SELECTOR, '[data-test-id="price-min-input"]')
    TO_BTN = (By.CSS_SELECTOR, '[data-test-id="price-max-input"]')
    APPLY_FILTER_BTN = (By.XPATH, '//button[text()="Apply filter"]')
    SEARCH_FILTER_BTN = {
        "mobile": (By.CSS_SELECTOR, '[class*="overflow-auto scrollbar-hide"] [data-test-id="search-and-filters-button"]'),
        "web": (By.CSS_SELECTOR, '[class*="scrollbar-hide select-none"] [data-test-id="search-and-filters-button"]')
    }
    PROJECT_CARDS = (By.CSS_SELECTOR, '[class*="outline-none"][data-test-id*="project-card"]')

    def filter_by_developer(self):
        self.wait_until_clickable_click(*self.platform_locator(self.DEVELOPER_BTN))
        self.wait_until_clickable(*self.AARK_DEVELOPER_BTN)
        self.real_click(*self.AARK_DEVELOPER_BTN)

    def filter_by_price_range(self):
        self.wait_until_clickable_click(*self.platform_locator(self.PRICE_BTN))
        self.wait_until_element_present(*self.FROM_BTN)
        self.input_text('1200000',*self.FROM_BTN)
        self.input_text('2000000',*self.TO_BTN)
        self.remove_mobile_keyboard()
        self.wait_until_clickable_click(*self.APPLY_FILTER_BTN)

    def verify_op_page_opened(self):
        self.wait_until_element_present(*self.platform_locator(self.SEARCH_FILTER_BTN))

    def verify_developer_filter(self):
        self.verify_partial_text_in_collection('Aark', *self.PROJECT_CARDS)

    def verify_price_range(self):
        self.verify_text('1.2M - 2M AED',*self.platform_locator(self.PRICE_BTN))
