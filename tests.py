from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class Tests:
    driver: webdriver

    def setup_method(self):
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--test-type")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(ChromeDriverManager("87.0.4280.20").install(), options=options)
        self.driver.wait = WebDriverWait(self.driver, 5)

    def teardown_method(self):
        self.driver.close()

    def test_lookup(self):
        self.driver.get("http://tictactoe.no/")
        self.driver.find_element_by_css_selector('.css-18t94o4.css-1dbjc4n.'
                                                 'r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73').click()
        print('Test Completed!')
        assert True


