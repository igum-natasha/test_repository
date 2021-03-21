from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


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
        self.driver.get("http://tictactoe.no/")
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()
        dark_style = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-vl818t.r-pm2fo."
                                                              "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                              "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                              "r-1mhb1uw")
        dark_style.click()
        self.driver.refresh()

    def teardown_method(self):
        self.driver.refresh()
        self.driver.close()

    def test_multiplayer(self):
        buttom_multiplayer = self.driver.find_element_by_css_selector('.css-18t94o4.css-1dbjc4n.'
                                                                      'r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        buttom_multiplayer.click()
        assert True

    def test_number_of_3_cells(self):
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
        assert 3 ** 2 == len(cells) - 5

    def test_number_of_4_cells(self):
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
        assert 4 ** 2 == len(cells) - 5

    def test_number_of_5_cells(self):
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
        assert 5 ** 2 == len(cells) - 5

    def test_enter_lobby_id(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        lobby_id = self.driver.find_element_by_css_selector("input.css-1cwyjr8.r-1wk2t95.r-f8cu29.r-1f0042m."
                                                             "r-jwli3a.r-adyw6z.r-eu3ka.r-xyro26.r-zt59i6."
                                                             "r-q4m81j.r-l0gwng")
        lobby_id.click()
        lobby_id.clear()
        lobby_id.send_keys('ddd')
        lobby_id.send_keys(Keys.RETURN)
        join = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                         "r-1otgn73")
        for e in join:
            if e.text == "JOIN":
                e.click()
        time.sleep(10)
        answer = self.driver.find_element_by_css_selector(".css-901oao.r-1erp77z.r-a023e6.r-vw2c0b.r-1tmtcfd.r-q4m81j")
        assert 'This lobby does not exist...' == answer.text

    def test_change_style_(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        first_style = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-zmljjp."
                                                               "r-t12b5v.r-rs99b7.r-1loqt21.r-ur6pnr.r-1777fci.r-crgep1"
                                                               ".r-1udh08x.r-bnwqim.r-1otgn73.r-1mhb1uw")
        first_style.click()

        background = self.driver.find_element_by_css_selector(".css-1dbjc4n.r-1awozwy.r-1ji381s.r-13awgt0.r-1777fci")
        assert background.value_of_css_property("background-color") == "rgba(230, 234, 235, 1)"

    def test_change_style_light(self):
        menu = self.driver. \
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

    def test_change_style_dark(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        dark_style = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-14lw9ot.r-pm2fo."
                                                              "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                              "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                              "r-1mhb1uw")
        dark_style.click()
        background = self.driver.find_element_by_css_selector(".css-1dbjc4n.r-1awozwy.r-blqegh.r-13awgt0.r-1777fci")
        assert background.value_of_css_property("background-color") == "rgba(42, 45, 52, 1)"

    def test_project_github(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        project = self.driver.find_element_by_xpath('//*[contains(text(), "Project on GitHub")]')
        print(project.get_attribute('class'))
        project.click()
        github = self.driver.window_handles[-1]
        self.driver.switch_to.window(github)
        assert self.driver.title == 'GitHub - andordavoti/tic-tac-toe-app: Online multiplayer ' \
                                    'Tic Tac Toe game for iOS, android and web.'

    def test_quit_game(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()

        new_game = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                            "r-1otgn73")
        for e in new_game:
            if e.text == "NEW GAME":
                e.click()
        time.sleep(10)
        quit_game = self.driver.find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.'
                                                              'r-1otgn73')
        for e in quit_game:
            if e.text == "QUIT GAME":
                e.click()
        assert self.driver.title == 'Tic Tac Toe'

    def test_online_game_3(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        buttom_num_3 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-14lw9ot."
                                                                "r-zmljjp.r-t12b5v.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        buttom_num_3.click()
        new_game = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                             "r-1otgn73")
        for e in new_game:
            if e.text == "NEW GAME":
                e.click()
        time.sleep(10)
        lobby = self.driver.\
            find_element_by_css_selector(".css-901oao.r-jwli3a.r-adyw6z.r-vw2c0b.r-9h1qh2.r-q4m81j").text
        self.driver.execute_script('window.open("https://tictactoe.no/")')
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        buttom_num_3 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-14lw9ot."
                                                                "r-zmljjp.r-t12b5v.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        buttom_num_3.click()
        lobby_id = self.driver.find_element_by_css_selector("input.css-1cwyjr8.r-1wk2t95.r-f8cu29.r-1f0042m."
                                                             "r-jwli3a.r-adyw6z.r-eu3ka.r-xyro26.r-zt59i6."
                                                             "r-q4m81j.r-l0gwng")
        lobby_id.click()
        lobby_id.clear()
        lobby_id.send_keys(lobby[1:])
        lobby_id.send_keys(Keys.RETURN)
        join = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                         "r-1otgn73")
        for e in join:
            if e.text == "JOIN":
                e.click()
        time.sleep(10)
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        print(len(cells))
        assert 3**2 == len(cells) - 5

    def test_online_game_4(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        buttom_num_4 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi."
                                                                "r-gxnn5r.r-17gur6a.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        buttom_num_4.click()
        new_game = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                             "r-1otgn73")
        for e in new_game:
            if e.text == "NEW GAME":
                e.click()
        time.sleep(10)
        lobby = self.driver.\
            find_element_by_css_selector(".css-901oao.r-jwli3a.r-adyw6z.r-vw2c0b.r-9h1qh2.r-q4m81j").text
        self.driver.execute_script('window.open("https://tictactoe.no/")')
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        buttom_num_4 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi."
                                                                "r-gxnn5r.r-17gur6a.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        buttom_num_4.click()
        lobby_id = self.driver.find_element_by_css_selector("input.css-1cwyjr8.r-1wk2t95.r-f8cu29.r-1f0042m."
                                                             "r-jwli3a.r-adyw6z.r-eu3ka.r-xyro26.r-zt59i6."
                                                             "r-q4m81j.r-l0gwng")
        lobby_id.click()
        lobby_id.clear()
        lobby_id.send_keys(lobby[1:])
        lobby_id.send_keys(Keys.RETURN)
        join = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                         "r-1otgn73")
        for e in join:
            if e.text == "JOIN":
                e.click()
        time.sleep(10)
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        print(len(cells))
        assert 4**2 == len(cells) - 5

    def test_online_game_5(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        buttom_num_5 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-pm2fo."
                                                                "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        buttom_num_5.click()
        new_game = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                             "r-1otgn73")
        for e in new_game:
            if e.text == "NEW GAME":
                e.click()
        time.sleep(10)
        lobby = self.driver.\
            find_element_by_css_selector(".css-901oao.r-jwli3a.r-adyw6z.r-vw2c0b.r-9h1qh2.r-q4m81j").text
        self.driver.execute_script('window.open("https://tictactoe.no/")')
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        buttom_num_5 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-pm2fo."
                                                                "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        buttom_num_5.click()
        lobby_id = self.driver.find_element_by_css_selector("input.css-1cwyjr8.r-1wk2t95.r-f8cu29.r-1f0042m."
                                                             "r-jwli3a.r-adyw6z.r-eu3ka.r-xyro26.r-zt59i6."
                                                             "r-q4m81j.r-l0gwng")
        lobby_id.click()
        lobby_id.clear()
        lobby_id.send_keys(lobby[1:])
        lobby_id.send_keys(Keys.RETURN)
        join = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                         "r-1otgn73")
        for e in join:
            if e.text == "JOIN":
                e.click()
        time.sleep(10)
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        print(len(cells))
        assert 5**2 == len(cells) - 5
