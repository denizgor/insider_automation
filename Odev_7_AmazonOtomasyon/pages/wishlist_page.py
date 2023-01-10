from Odev_7_AmazonOtomasyon.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class WishlistPage(BasePage):
    DELETE_ITEM = (By.CSS_SELECTOR, "[name='submit.deleteItem']")
    WISHLISTED_PRODUCT = (By.CSS_SELECTOR, "h2.a-size-base")
    DELETED_TEXT = (By.CLASS_NAME, "a-alert-content")

    def delete_item(self):
        self.click_element(*self.DELETE_ITEM)

    def get_wishlisted_product_text(self):
        return self.find_element(*self.WISHLISTED_PRODUCT).text

    def get_deleted_item_text(self, index):
        return self.find_elements(index, *self.DELETED_TEXT).text
