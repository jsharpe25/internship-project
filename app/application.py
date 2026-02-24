from pages.base_page import Page
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.side_menu_page import SideMenuPage

class Application:

    def __init__(self, driver, is_mobile=False):

        self.base_page = Page(driver, is_mobile)
        self.is_mobile = is_mobile
        self.main_page = MainPage(driver, is_mobile)
        self.off_plan_page = OffPlanPage(driver, is_mobile)
        self.side_menu_page = SideMenuPage(driver, is_mobile)
