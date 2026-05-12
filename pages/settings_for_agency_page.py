from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SettingsForAgencyPage(Page):
    CONTACT_FORM = (By.XPATH, '//label[text()="Contact us for details"]')

    def verify_agency_page(self):
        self.verify_url_contains('/buy-plan-company')

    def scroll_to_form(self):
        self.wait_until_element_present(*self.CONTACT_FORM)
        self.scroll_to_element(*self.CONTACT_FORM)

    def verify_contact_us_form(self):
        self.wait_until_element_visible(*self.CONTACT_FORM)
        self.verify_partial_text('Contact us',*self.CONTACT_FORM)
