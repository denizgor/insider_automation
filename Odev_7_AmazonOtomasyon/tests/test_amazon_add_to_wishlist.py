from Odev_7_AmazonOtomasyon.tests.base_test import BaseTest
from Odev_7_AmazonOtomasyon.pages.home_page import HomePage


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
        login_page = home_page.click_accounts()

        self.assertTrue(login_page.is_on_login_page())
        login_page.send_email(self.email_text)
        login_page.click_continue()
        login_page.send_password(self.password_text)
        login_page.click_submit()

        home_page.send_search_keys(self.search_keys)
        search_result_page = home_page.submit_search()

        self.assertIn(self.search_keys, search_result_page.get_search_term_text(), "Search and result do not match.")
        search_result_page.go_to_next_page()
        self.assertEqual(self.search_page, search_result_page.get_selected_page_text(), "Current page isn't 2nd page.")
        product_page = search_result_page.get_a_product(self.selected_product_index)

        chosen_product_name = product_page.get_product_name()
        product_page.add_to_wishlist()
        product_page.close_popup()
        product_page.hover_accounts()
        wishlist_page = product_page.go_to_wishlist()

        self.assertEqual(chosen_product_name, wishlist_page.get_wishlisted_product_text())
        wishlist_page.delete_item()
        self.assertTrue(wishlist_page.is_item_deleted(self.wishlist_page_prod_index))

    def tearDown(self):
        self.driver.quit()