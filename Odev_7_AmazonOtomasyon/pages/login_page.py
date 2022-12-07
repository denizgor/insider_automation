from Odev_7_AmazonOtomasyon.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    LOGIN = (By.CSS_SELECTOR, "[alt='Giriş Yapma ve Güvenlik']")

    def click_login(self):
        self.click_element(*self.LOGIN)