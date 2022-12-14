from selenium.webdriver.common.by import By

from Odev_7_AmazonOtomasyon.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN = (By.CSS_SELECTOR, "[alt='Giriş Yapma ve Güvenlik']")
    EMAIL_FIELD = (By.ID, "ap_email")
    PASSWORD_FIELD = (By.ID, "ap_password")
    CONTINUE_BTN = (By.CSS_SELECTOR, "input#continue")
    SUBMIT_BTN = (By.CSS_SELECTOR, "input#signInSubmit")

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



