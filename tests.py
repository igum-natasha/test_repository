from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Tests:
    driver: webdriver

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.wait = WebDriverWait(self.driver, 5)

    def teardown_method(self):
        self.driver.close()

    def test_lookup(self):
        self.driver.get("http://tictactoe.no/")
        self.driver.find_element_by_css_selector('.css-18t94o4.css-1dbjc4n.'
                                                 'r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73').click()
        print('Test Completed!')
        assert True


