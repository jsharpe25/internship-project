from pages.base_page import Page
from pages.main_page import MainPage
from pages.off_plan_page import OffPlanPage
from pages.settings_page import SettingsPage
from pages.settings_for_agency_page import SettingsForAgencyPage
from pages.settings_my_clients_page import SettingsMyClientsPage
from pages.sidebar_page import SidebarPage
from pages.university_page import UniversityPage

class Application:

    def __init__(self, driver, is_mobile=False):

        self.base_page = Page(driver, is_mobile)
        self.is_mobile = is_mobile
        self.main_page = MainPage(driver, is_mobile)
        self.off_plan_page = OffPlanPage(driver, is_mobile)
        self.settings_page = SettingsPage(driver, is_mobile)
        self.settings_for_agency_page = SettingsForAgencyPage(driver, is_mobile)
        self.settings_my_clients_page = SettingsMyClientsPage(driver, is_mobile)
        self.sidebar_page = SidebarPage(driver, is_mobile)
        self.university_page = UniversityPage(driver, is_mobile)
