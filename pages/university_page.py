from pages.base_page import Page
from selenium.webdriver.common.by import By

class UniversityPage(Page):
    CALENDAR_BTN = (By.CSS_SELECTOR, '.university-menu a[href="/calendar"]')
    BALI_BTN = (By.CSS_SELECTOR, 'a[href="/university-realestate"]')
    CONTENT_SECTIONS = [
        (
            "Bali Course Lessons",
            (By.XPATH, '//*[normalize-space()="Bali Course Lessons"]'),
            (By.XPATH, '(//a[@wized="courseVideoBlock"])[1]')
        ),
        (
            "Q/A sessions",
            (By.XPATH, '//*[normalize-space()="Q/A sessions"]'),
            (By.XPATH, '(//a[@wized="sessionVideoBlock"])[1]')
        ),
        (
            "Discover last podcast",
            (By.XPATH, '//*[normalize-space()="Discover last podcast"]'),
            (By.XPATH, '(//div[@wized="coursePodcastBlock"])[1]')
        )
    ]

    def verify_university_page(self):
        self.verify_url_contains('university-podcast')

    def click_calendar_option(self):
        self.wait_until_clickable_click(*self.CALENDAR_BTN)

    def click_bali_option(self):
        self.wait_until_clickable_click(*self.BALI_BTN)

    def verify_content_headers_and_cards(self):
        for section_name, section_locator, card_locator in self.CONTENT_SECTIONS:
            self.scroll_to_element(*section_locator)
            self.wait_until_element_visible(*section_locator)
            self.verify_text(section_name, *section_locator)
            self.wait_until_element_visible(*card_locator)
            cards = self.find_elements(*card_locator)
            assert cards, f'No card found under "{section_name}"'
