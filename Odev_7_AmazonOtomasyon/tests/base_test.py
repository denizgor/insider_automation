import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):
    base_url = "https://www.amazon.com.tr/"
    wait_duration = 10

    def setUp(self):
        option = Options()
        option.add_argument("--start-maximized")
        option.add_argument("--disable-extensions")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(self.wait_duration)