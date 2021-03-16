from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class Tests:
    def setup_method(self):
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--test-type")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-infobars")
        self.driver = webdriver.Chrome(".\\chromedriver.exe", options=options)
        self.driver.wait = WebDriverWait(self.driver, 5)
        #self.driver.refresh()

    def teardown_method(self):
        self.driver.refresh()
        self.driver.close()

    def test_multiplayer(self):
        self.driver.get("http://tictactoe.no/")
        buttom_multiplayer = self.driver.find_element_by_css_selector('.css-18t94o4.css-1dbjc4n.'
                                                                      'r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        buttom_multiplayer.click()
        self.driver.refresh()
        assert True

    def test_number_of_3_cells(self):
        self.driver.get("http://tictactoe.no/")
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        buttom_num_3 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-14lw9ot.r-zmljjp."
                                                                "r-t12b5v.r-rs99b7.r-1loqt21.r-ur6pnr.r-1777fci."
                                                                "r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73.r-1mhb1uw")
        buttom_num_3.click()
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        self.driver.refresh()
        assert 3**2 == len(cells)-5

    def test_number_of_4_cells(self):
        self.driver.get("http://tictactoe.no/")
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        buttom_num_4 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-gxnn5r."
                                                                "r-17gur6a.r-rs99b7.r-1loqt21.r-ur6pnr.r-1777fci."
                                                                "r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73.r-1mhb1uw")
        buttom_num_4.click()
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        self.driver.refresh()
        assert 4**2 == len(cells)-5

    def test_number_of_5_cells(self):
        self.driver.get("http://tictactoe.no/")
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        buttom_num_5 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-pm2fo."
                                                                "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        buttom_num_5.click()
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        self.driver.refresh()
        assert 5**2 == len(cells)-5

    def test_change_style_(self):
        self.driver.get("http://tictactoe.no/")
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        first_style = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-14lw9ot.r-zmljjp."
                                                               "r-t12b5v.r-rs99b7.r-1loqt21.r-ur6pnr.r-1777fci.r-crgep1"
                                                               ".r-1udh08x.r-bnwqim.r-1otgn73.r-1mhb1uw")
        first_style.click()
        background = self.driver.find_element_by_css_selector(".css-1dbjc4n.r-1awozwy.r-blqegh.r-13awgt0.r-1777fci")
        assert background.value_of_css_property("background-color") == "rgba(42, 45, 52, 1)"
        self.driver.refresh()

    def test_change_style_light(self):
        self.driver.get("http://tictactoe.no/")
        menu = self.driver.\
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        light_style = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-gxnn5r."
                                                               "r-17gur6a.r-rs99b7.r-1loqt21.r-ur6pnr.r-1777fci."
                                                               "r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73.r-1mhb1uw")
        light_style.click()
        background = self.driver.find_element_by_css_selector(".css-1dbjc4n.r-1awozwy.r-1ji381s.r-13awgt0.r-1777fci")
        assert background.value_of_css_property("background-color") == "rgba(230, 234, 235, 1)"
        self.driver.refresh()

    def test_change_style_dark(self):
        self.driver.get("http://tictactoe.no/")
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        dark_style = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-pm2fo."
                                                               "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                               "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                               "r-1mhb1uw")
        dark_style.click()
        self.driver.refresh()
        background = self.driver.find_element_by_css_selector(".css-1dbjc4n.r-1awozwy.r-blqegh.r-13awgt0.r-1777fci")
        assert background.value_of_css_property("background-color") == "rgba(42, 45, 52, 1)"

