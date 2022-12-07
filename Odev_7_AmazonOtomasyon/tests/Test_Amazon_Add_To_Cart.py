

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




#PATH = "C:\\Users\\D\\Desktop\\Software Testing\\edgedriverwin64\\msedgedriver.exe"
#driver = webdriver.Edge(PATH)
service = Service( "C:\\Users\\D\\Desktop\\Software Testing\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
webdriver.chrome

class Test_Amazon_Add_To_Cart:
    wait = WebDriverWait(driver, 10)
    mainpage = driver.get('https://www.amazon.com.tr')
    MAINPAGE = driver.get('https://www.amazon.com.tr')
    SEARCHBAR = driver.find_element(By.ID, 'twotabsearchtextbox')


    driver.get('https://www.amazon.com.tr')
    # driver.get(search)
    #driver.find_element(By.ID, "sp-cc-rejectall-link").click()
    driver.maximize_window()

    try:

        driver.find_element(By.ID, 'sp-cc-accept').click()
        SEARCHBAR = wait.until(EC.element_to_be_clickable((By.ID,'twotabsearchtextbox')))
        SEARCHBAR.click()
        SEARCHBAR.send_keys('laptop')
    except:
        driver.quit()


    # Sample_Projects

    #ANASAYFA

    #Giriş
    #Cookies
    #id = "sp-cc-accept"

    #deny cookies
    #id="sp-cc-rejectall-link"

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
    #
Test_Amazon_Add_To_Cart

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
