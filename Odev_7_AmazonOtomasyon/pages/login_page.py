from selenium.webdriver.common.by import By

from Odev_7_AmazonOtomasyon.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN = (By.CSS_SELECTOR, "[alt='Giriş Yapma ve Güvenlik']")
    EMAIL_FIELD = (By.ID, "ap_email")
    PASSWORD_FIELD = (By.ID, "ap_password")
    CONTINUE_BTN = (By.ID, "continue")
    SUBMIT_BTN = (By.ID, "signInSubmit")

    def is_on_login_page(self):
        return self.find_element(*self.EMAIL_FIELD)

    def click_login(self):
        self.click_element(*self.LOGIN)

    def send_email(self, email):
        self.send_text(email, *self.EMAIL_FIELD)

    def send_password(self, password):
        self.send_text(password, *self.PASSWORD_FIELD)

    def click_continue(self):
        self.click_element(*self.CONTINUE_BTN)

    def click_submit(self):
        self.click_element(*self.SUBMIT_BTN)