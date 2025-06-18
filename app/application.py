from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Pages.target_search_page import OpenTargetPage
from Pages.basepage import Page


class Application:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(20)

        self.page = Page(self.driver)
        self.open_target_page = OpenTargetPage(self.driver)
        self.search_for = OpenTargetPage(self.driver)
        self.locate_item = OpenTargetPage(self.driver)
        self.verify_title = OpenTargetPage(self.driver)
