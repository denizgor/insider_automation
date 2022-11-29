import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestCheckLcwAutomation(unittest.TestCase):
    EV_YASAM_CAT = (By.LINK_TEXT, "EV & YAŞAM")
    CATAL_KASIK_CAT = (By.LINK_TEXT, "Çatal, Kaşık ve Bıçak")
    CATAL_KASIK_BRD = (By.CLASS_NAME, "lcw-breadcrumb__item-list__item:last-child")
    PRODUCT_CARD = (By.CSS_SELECTOR, "div.product-card")
    ADD_TO_CART_BTN = (By.LINK_TEXT, "SEPETE EKLE")
    CART_COUNT_BADGE = (By.CSS_SELECTOR, "span.badge-circle")
    PROCEED_TO_PAY_TXT = (By.LINK_TEXT, "ÖDEME ADIMINA GEÇ")
    DELETE_ITEM_ICON = (By.CSS_SELECTOR, "[title='Sil']")
    DELETE_BTN = (By.LINK_TEXT, "Sil")
    EMPTY_CART_TEXT = (By.CLASS_NAME, "cart-empty-title")
    CART_HEADER = (By.CSS_SELECTOR, "div.cart-header")
    LCW_LOGO = (By.CSS_SELECTOR, "a.main-header-logo")


    base_url = "https://www.lcwaikiki.com/tr-TR/TR"
    catal_kasik_brd = "Çatal, Kaşık, Bıçak Setleri"
    proceed_to_pay_txt = "ÖDEME ADIMINA GEÇ"
    wait_duration = 10

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(self.wait_duration)

        self.wait = WebDriverWait(self.driver, self.wait_duration)

    def test_check_lcw_automation(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.EV_YASAM_CAT)).perform()
        actions.move_to_element(self.driver.find_element(*self.CATAL_KASIK_CAT)).click().perform()

        self.assertEqual(self.catal_kasik_brd, self.driver.find_element(*self.CATAL_KASIK_BRD).text,
                         "Breadcrumb assertion is false.")

        self.driver.find_elements(*self.PRODUCT_CARD)[1].click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(*self.ADD_TO_CART_BTN)),
                        "Add to Cart button is not present.")

        self.driver.find_element(*self.ADD_TO_CART_BTN).click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(*self.CART_COUNT_BADGE)),
                        "Sepete ürün eklenmedi.")

        self.driver.find_element(*self.CART_COUNT_BADGE).click()
        self.assertIn("Sepetim", self.driver.find_element(*self.CART_HEADER).text,
                      "Couldn't find 'Sepetim' in cart header.")

        self.driver.find_element(*self.DELETE_ITEM_ICON).click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(*self.DELETE_BTN)),
                        "'Item Delete Modal' not visible.")

        self.driver.find_element(*self.DELETE_BTN).click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(*self.EMPTY_CART_TEXT)),
                        "Cart is not empty.")

        self.driver.find_element(*self.LCW_LOGO).click()
        self.assertEqual(self.base_url, self.driver.current_url,
                         "Is not on mainpage.")

    def tearDown(self):
        self.driver.quit()


