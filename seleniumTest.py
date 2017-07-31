import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RentCalculation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_page_title(self):
        driver = self.driver
        driver.get("https://yevrap.github.io/housingCalculator/")

        self.assertEqual("Rent Calculator", driver.title)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()