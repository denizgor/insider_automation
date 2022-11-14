import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestCheckLCWAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.lcwaikiki.com/tr-TR/TR")
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)

    def test_check_LCW_automation(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.LINK_TEXT, "EV & YAŞAM")).perform()
        actions.move_to_element(self.driver.find_element(By.LINK_TEXT, "Çatal, Kaşık ve Bıçak")).click().perform()

        self.assertEqual("Çatal, Kaşık, Bıçak Setleri", self.driver.find_element(
            By.CLASS_NAME, "lcw-breadcrumb__item-list__item:last-child").text, "Breadcrumb assertion is false.")

        self.driver.find_elements(By.CSS_SELECTOR, "div.product-card")[2].click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(
            By.LINK_TEXT, "SEPETE EKLE")), "Add to Cart button is not present.")

        self.driver.find_element(By.LINK_TEXT, "SEPETE EKLE").click()
        self.assertEqual("SEPETE EKLENDİ", self.driver.find_element(
            By.LINK_TEXT, "SEPETE EKLENDİ").text, "Couldn't find 'SEPETE EKLENDİ'.")

        self.driver.find_element(By.CSS_SELECTOR, "span.badge-circle").click()
        self.assertEqual("ÖDEME ADIMINA GEÇ", self.driver.find_element(
            By.LINK_TEXT, "ÖDEME ADIMINA GEÇ").text, "Couldn't find 'ÖDEME ADIMINA GEÇ'.")

        self.driver.find_element(By.CSS_SELECTOR, "[title='Sil']").click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(
            By.LINK_TEXT, "Sil")), "Item Delete Modal not visible.")

        self.driver.find_element(By.LINK_TEXT, "Sil").click()
        self.assertTrue(EC.presence_of_element_located(self.driver.find_element(
            By.CLASS_NAME, "cart-empty-title")), "Cart is not empty.")

        self.driver.find_element(By.CSS_SELECTOR, "a.main-header-logo").click()
        self.assertEqual("https://www.lcwaikiki.com/tr-TR/TR", self.driver.current_url, "Is not on mainpage.")

    def tearDown(self) -> None:
        self.driver.quit()
