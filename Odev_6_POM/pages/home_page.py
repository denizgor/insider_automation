from Odev_6_POM.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    EV_YASAM_CAT = (By.LINK_TEXT, "EV & YAŞAM")
    CATAL_KASIK_CAT = (By.LINK_TEXT, "Çatal, Kaşık ve Bıçak")

    def click_ev_yasam_cat(self):
        self.hover_element(*self.EV_YASAM_CAT)

    def click_catal_kasik(self):
        self.hover_element(*self.CATAL_KASIK_CAT)
