from selenium.webdriver.common.by import By

from Odev_7_AmazonOtomasyon.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN = (By.CSS_SELECTOR, "[alt='Giriş Yapma ve Güvenlik']")
    EMAIL_FIELD = (By.ID, "ap_email")

    def click_login(self):
        self.click_element(*self.LOGIN)

    def fill_email(self, email):
        self.fill_field(*self.EMAIL_FIELD, email)
