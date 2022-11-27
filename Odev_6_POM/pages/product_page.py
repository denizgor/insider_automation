from selenium.webdriver.common.by import By
from Odev_6_POM.pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.LINK_TEXT, "SEPETE EKLE")
    CART_COUNT_BADGE = (By.CSS_SELECTOR, "span.badge-circle")

    def wait_add_to_cart_btn(self):
        self.wait_element(self.ADD_TO_CART_BTN, "Add to Cart button is not present.")

    def click_add_to_cart_btn(self):
        self.click_element(*self.ADD_TO_CART_BTN)
