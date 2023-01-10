from Odev_7_AmazonOtomasyon.pages.base_page import BasePage
from Odev_7_AmazonOtomasyon.pages.wishlist_page import WishlistPage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_TO_WISHLIST_BTN = (By.ID, "add-to-wishlist-button-submit")
    CLOSE_POPUP_BTN = (By.CLASS_NAME, "a-button-close")
    ACCOUNTS_AND_LISTS = (By.ID, "nav-link-accountList")
    WISHLIST_TEXT = (By.LINK_TEXT, "Alışveriş Listesi")
    PRODUCT = (By.ID, "productTitle")

    def add_to_wishlist(self):
        self.click_element(*self.ADD_TO_WISHLIST_BTN)

    def get_product_name(self):
        return self.find_element(*self.PRODUCT).text

    def close_popup(self):
        self.click_element(*self.CLOSE_POPUP_BTN)

    def hover_accounts(self):
        self.hover_element(*self.ACCOUNTS_AND_LISTS)

    def go_to_wishlist(self):
        self.click_element(*self.WISHLIST_TEXT)

        return WishlistPage(self.driver)