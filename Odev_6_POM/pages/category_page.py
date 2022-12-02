from Odev_6_POM.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CategoryPage(BasePage):

    PRODUCT_CARD = (By.CSS_SELECTOR, "div.product-card")
    CATAL_KASIK_BRD = (By.CLASS_NAME, "li.lcw-breadcrumb__item-list__item:last-child")

    def click_a_product(self):
        self.find_elements(1, *self.PRODUCT_CARD).click()

    def get_breadcrumb(self):
        self.text(self.CATAL_KASIK_BRD)
