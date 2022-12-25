from selenium.webdriver.common.by import By

from Odev_7_AmazonOtomasyon.pages.base_page import BasePage


class HomePage(BasePage):
    ACCOUNTS = (By.ID, "nav-link-accountList")
    COOKIE_PERMISSION = (By.ID, "sp-cc-accept")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SUBMIT_SEARCH_BTN = (By.ID, "nav-search-submit-button")

    def click_accounts(self):
        self.click_element(*self.ACCOUNTS)

    def accept_cookies(self):
        self.click_element(*self.COOKIE_PERMISSION)

    def send_search_keys(self, text):
        self.send_text(text, *self.SEARCH_BOX)

    def submit_search(self):
        self.click_element(*self.SUBMIT_SEARCH_BTN)
