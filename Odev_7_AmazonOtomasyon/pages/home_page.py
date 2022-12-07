from Odev_7_AmazonOtomasyon.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    ACCOUNTS = (By.LINK_TEXT, "Hesabım")

    def click_accounts(self):
        self.click_element(*self.ACCOUNTS)
