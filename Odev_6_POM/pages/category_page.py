from Odev_6_POM.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CategoryPage(BasePage):

    PRODUCT_CARD = (By.CSS_SELECTOR, "div.product-card")

    def click_a_product(self):
        self.find_elements(*self.PRODUCT_CARD, 1).click()
