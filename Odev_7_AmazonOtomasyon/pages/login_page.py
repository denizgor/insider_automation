from selenium.webdriver.common.by import By

from Odev_7_AmazonOtomasyon.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN = (By.CSS_SELECTOR, "[alt='Giriş Yapma ve Güvenlik']")

    def click_login(self):
        self.click_element(*self.LOGIN)
