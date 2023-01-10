from Odev_7_AmazonOtomasyon.tests.base_test import BaseTest
from Odev_7_AmazonOtomasyon.pages.home_page import HomePage
from Odev_7_AmazonOtomasyon.pages.login_page import LoginPage
from Odev_7_AmazonOtomasyon.pages.search_result_page import SearchResultPage
from Odev_7_AmazonOtomasyon.pages.product_page import ProductPage
from Odev_7_AmazonOtomasyon.pages.wishlist_page import WishlistPage
from selenium.webdriver.support import expected_conditions as EC


class TestAmazonAddToWishlist(BaseTest):
    email_text = "e7cd978d@opayq.com"
    password_text = "LJsxBU.22G"
    search_keys = "samsung"
    search_page = "2"
    selected_product_index = 9
    wishlist_page_prod_index = 11

    def test_amazon_add_to_wishlist(self):
        home_page = HomePage(self.driver)
        self.assertEqual(self.base_url, self.driver.current_url, "The base_url doesn't match current URL!")
        home_page.accept_cookies()
        home_page.click_accounts()

        login_page = LoginPage(self.driver)
        self.assertTrue(EC.presence_of_element_located(login_page.LOGIN))
        login_page.send_email(self.email_text)
        login_page.click_continue()
        login_page.send_password(self.password_text)
        login_page.click_submit()

        home_page.send_search_keys(self.search_keys)
        home_page.submit_search()

        search_result_page = SearchResultPage(self.driver)
        self.assertIn(self.search_keys, search_result_page.get_search_term_text(), "Search and result do not match.")
        search_result_page.go_to_next_page()
        self.assertEqual(self.search_page, search_result_page.get_selected_page_text(), "Current page isn't 2nd page.")

        search_result_page.get_a_product(self.selected_product_index)

        product_page = ProductPage(self.driver)
        chosen_product_name = product_page.get_product_name()
        product_page.add_to_wishlist()
        product_page.close_popup()
        product_page.hover_accounts()
        product_page.go_to_wishlist()

        wishlist_page = WishlistPage(self.driver)
        self.assertEqual(chosen_product_name, wishlist_page.get_wishlisted_product_text())
        wishlist_page.delete_item()
        self.assertTrue(
            EC.presence_of_element_located(wishlist_page.get_deleted_item_text(self.wishlist_page_prod_index)))

    def tearDown(self) -> None:
        self.driver.quit()
