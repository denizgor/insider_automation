from Odev_7_AmazonOtomasyon.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):
    NEXT_PAGE_BTN = (By.LINK_TEXT, "Sonraki")
    SEARCH_TERM = (By.CSS_SELECTOR, "[data-component-type = 's-result-info-bar']")
    SELECTED_PAGE = (By.CLASS_NAME, "s-pagination-selected")
    PRODUCT = (By.CSS_SELECTOR, ".a-section.a-spacing-base")

    def go_to_next_page(self):
        self.click_element(*self.NEXT_PAGE_BTN)

    def get_search_term_text(self):
        return self.find_element(*self.SEARCH_TERM).text

    def get_selected_page_text(self):
        return self.find_element(*self.SELECTED_PAGE).text

    def get_a_product(self, index):
        self.find_elements(index, *self.PRODUCT).click()


