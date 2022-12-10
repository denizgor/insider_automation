from selenium.webdriver.common.by import By

from Odev_7_AmazonOtomasyon.pages.base_page import BasePage


class HomePage(BasePage):
    ACCOUNTS = (By.LINK_TEXT, "Hesabım")
    COOKIE_PERMISSION = (By.ID, "sp-cc-accept")

    def click_accounts(self):
        self.click_element(*self.ACCOUNTS)

    def accept_cookies(self):
        self.click_element(*self.COOKIE_PERMISSION)