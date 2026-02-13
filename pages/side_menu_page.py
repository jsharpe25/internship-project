from pages.base_page import Page
from selenium.webdriver.common.by import By

class SideMenuPage(Page):
    OFF_PLAN_BTN = (By.CSS_SELECTOR, '.menu-button-block.w-inline-block[wized="newOffPlanLink"]')

    def click_off_plan_tab(self):
        self.wait_until_clickable_click(*self.OFF_PLAN_BTN)
