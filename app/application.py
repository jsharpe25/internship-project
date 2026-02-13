from pages.base_page import Page
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.side_menu_page import SideMenuPage

class Application:

    def __init__(self, driver):

        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.side_menu_page = SideMenuPage(driver)
