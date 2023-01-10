from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.find_element(*locator).click()

    def send_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def hover_element(self, *locator):
        self.actions.move_to_element(self.find_element(*locator)).perform()

    def wait_element(self, method, message=""):
        return self.wait.until(EC.presence_of_element_located(method), message)

    def find_elements(self, index, *element):
        return self.driver.find_elements(*element)[index]
