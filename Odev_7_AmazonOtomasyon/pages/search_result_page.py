from Odev_7_AmazonOtomasyon.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultPage(BasePage):
    NEXT_PAGE_BTN = (By.LINK_TEXT, "Sonraki")

    def go_to_next_page(self):
        self.click_element(*self.NEXT_PAGE_BTN)