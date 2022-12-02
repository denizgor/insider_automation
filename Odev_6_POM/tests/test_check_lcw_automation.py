import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from Odev_6_POM.pages.product_page import ProductPage
from Odev_6_POM.tests.base_test import BaseTest
from Odev_6_POM.pages.home_page import HomePage
from Odev_6_POM.pages.category_page import CategoryPage


class TestCheckLCWAutomation(BaseTest):
    CATAL_KASIK_BRD = (By.CLASS_NAME, "lcw-breadcrumb__item-list__item:last-child")
    PROCEED_TO_PAY_TXT = (By.LINK_TEXT, "ÖDEME ADIMINA GEÇ")
    DELETE_ITEM_ICON = (By.CSS_SELECTOR, "[title='Sil']")
    DELETE_BTN = (By.LINK_TEXT, "Sil")
    EMPTY_CART_TEXT = (By.CLASS_NAME, "cart-empty-title")
    LCW_LOGO = (By.CSS_SELECTOR, "a.main-header-logo")

    proceed_to_pay_txt = "ÖDEME ADIMINA GEÇ"
    catal_kasik_brd = "Çatal, Kaşık, Bıçak Setleri"

    def test_check_lcw_automation(self):
        home_page = HomePage(self.driver)
        home_page.hover_ev_yasam_cat()
        home_page.click_catal_kasik()
        self.assertEqual(self.catal_kasik_brd, home_page.get_text(self.CATAL_KASIK_BRD), "Breadcrumb assertion is false.")

        # self.driver.find_elements(*self.PRODUCT_CARD)[1].click()
        category_page = CategoryPage(self.driver)
        category_page.click_a_product()

        product_page = ProductPage(self.driver)
        self.assertTrue(product_page.wait_add_to_cart_btn(), "Add to Cart button is not present.")
        # self.assertTrue(EC.presence_of_element_located(self.driver.find_element(*self.ADD_TO_CART_BTN)),
        #                "Add to Cart button is not present.")

        product_page = ProductPage(self.driver)

        self.driver.find_element(*self.ADD_TO_CART_BTN).click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(*self.CART_COUNT_BADGE)),
                        "Sepete ürün eklenmedi.")

        self.driver.find_element(*self.CART_COUNT_BADGE).click()
        self.assertEqual(self.proceed_to_pay_txt, self.driver.find_element(*self.PROCEED_TO_PAY_TXT).text,
                         "Couldn't find 'ÖDEME ADIMINA GEÇ'.")

        self.driver.find_element(*self.DELETE_ITEM_ICON).click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(*self.DELETE_BTN)),
                        "Item Delete Modal not visible.")

        self.driver.find_element(*self.DELETE_BTN).click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(*self.EMPTY_CART_TEXT)),
                        "Cart is not empty.")

        self.driver.find_element(*self.LCW_LOGO).click()
        self.assertEqual(self.base_url, self.driver.current_url,
                         "Is not on mainpage.")

    def tearDown(self):
        self.driver.quit()
