from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Odev_7_AmazonOtomasyon.pages.home_page import HomePage
from Odev_7_AmazonOtomasyon.pages.login_page import LoginPage
from Odev_7_AmazonOtomasyon.tests.base_test import BaseTest


class TestAmazonAddToWishlist(BaseTest):
    SEARCHBAR = (By.ID, 'twotabsearchtextbox')

    email_text = "e7cd978d@opayq.com"
    password_text = "LJsxBU.22G"

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



    def tearDown(self) -> None:
        self.driver.quit()

  

    # ANASAYFA

    # Giriş
    # Cookies
    # id = "sp-cc-accept"

    # deny cookies
    # id="sp-cc-rejectall-link"

    # $("#nav-link-accountList-nav-line-1")
    #
    #
    # #Siparişler
    # $("#nav-orders")
    #
    # #Sepet
    # $("#nav-cart")
    #
    #
    # #Searchbox-Dropdown
    # $("#searchDropdownBox")
    #
    # #Searchbox
    # $("#twotabsearchtextbox")
    #
    # #Konum
    # $("#nav-global-location-data-modal-action")
    #
    # #Logo
    # $("#nav-logo-sprites")
    #





# Amazon Test Task
#
# 1. http://www.amazon.com sitesine gidilecek ve anasayfanın açıldığını assertion ile onaylatılacak.
#
# 2.Login ekranını açıp, bir kullanıcı ile login olunacak ( daha önce siteye üyeliğiniz varsa o olabilir. )
#
# 3.Ekranin üstündeki Search alanına 'samsung' yazıp ara butonuna tıklanılacak.
#
# 4.Gelen sayfada samsung icin sonuc bulunduğu onaylatılacak.
#
# 5.Arama sonuçlarından 2. sayfaya tıklanıp ve açılan sayfada 2. sayfanin şu an gösterimde olduğunu onaylatılacak.
#
# 6.Üstten 3. ürünün içindeki 'Add to List' butonuna tıklatılacak.
#
# 7.Ekranin en üstündeki 'List' linkine tıklanarak içerisinden Wish listi seçilecek.
#
# 8.Açılan sayfada bir onceki sayfada izlemeye alınmış ürünün bulunduğu onaylatılacak.
#
# 9.Favorilere alınan bu ürünün yanındaki 'Delete' butonuna basılarak, favorilerimden çıkarılacak.
#
# 10. Sayfada bu ürünün artık favorilere alınmadığı onaylatılacak.


