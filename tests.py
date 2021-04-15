import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as op
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
import time

driver: webdriver

 
@pytest.fixture(params=['firefox', 'chrome'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--test-type")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-infobars")
        driver = webdriver.Chrome(".\\chromedriver.exe", options=options)
    if request.param == 'firefox':
        options = op()
        binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
        options.binary = binary
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-setuid-sandbox")
        cap = DesiredCapabilities().FIREFOX.copy()
        cap['marionette'] = True
        time.sleep(30)
        driver = webdriver.Firefox(capabilities=cap,
                                   executable_path=r"geckodriver.exe",
                                   options=options)
        driver.implicitly_wait(20)
    request.cls.driver = driver
    driver.wait = WebDriverWait(driver, 5)
    driver.get("http://tictactoe.no/")
    menu = driver. \
        find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
    for e in menu:
        if e.text == "SETTINGS":
            e.click()
    # r-vl818t.
    dark_style = driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-pm2fo."
                                                          "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                          "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                          "r-1mhb1uw")
    dark_style.click()


@pytest.mark.usefixtures("init_driver")
class BaseClassTests:
    pass


class Tests(BaseClassTests):
    def setup_method(self):
        self.driver.refresh()

    def teardown_method(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    @pytest.mark.new_feature
    @pytest.mark.button
    def test_multiplayer(self):
        button_multiplayer = self.driver.find_element_by_css_selector('.css-18t94o4.css-1dbjc4n.'
                                                                      'r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        button_multiplayer.click()
        assert True

    @pytest.mark.number_cells
    def test_number_of_3_cells(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        button_num_3 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-14lw9ot.r-zmljjp."
                                                                "r-t12b5v.r-rs99b7.r-1loqt21.r-ur6pnr.r-1777fci."
                                                                "r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73.r-1mhb1uw")
        button_num_3.click()
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        assert 3 ** 2 == len(cells) - 5

    @pytest.mark.number_cells
    def test_number_of_4_cells(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        button_num_4 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-gxnn5r."
                                                                "r-17gur6a.r-rs99b7.r-1loqt21.r-ur6pnr.r-1777fci."
                                                                "r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73.r-1mhb1uw")
        button_num_4.click()
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        assert 4 ** 2 == len(cells) - 5

    @pytest.mark.number_cells
    def test_number_of_5_cells(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        button_num_5 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-pm2fo."
                                                                "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        button_num_5.click()
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        assert 5 ** 2 == len(cells) - 5
    
    @pytest.mark.new_feature
    @pytest.mark.enter
    def test_enter_lobby_id(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        lobby_id = self.driver.find_element_by_css_selector("input.css-1cwyjr8.r-1wk2t95.r-f8cu29,r-1f0042m.r-jwli3a."
                                                            "r-adyw6z.r-eu3ka.r-1elzhzw.r-zt59i6.r-q4m81j.r-l0gwng")
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
        answer = self.driver.find_elements_by_css_selector(".css-901oao")
        titles = [elem.text for elem in answer]
        assert 'This lobby does not exist...' in titles
    
    @pytest.mark.style
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

        background = self.driver.find_element_by_css_selector(".css-1dbjc4n.r-1awozwy.r-blqegh.r-13awgt0.r-1777fci")
        hex_color = Color.from_string(background.value_of_css_property("background-color")).hex
        assert hex_color == "#2a2d34"

    @pytest.mark.new_tab
    def test_project_github(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        project = self.driver.find_element_by_xpath('//*[contains(text(), "Project on GitHub")]')
        project.click()
        time.sleep(10)
        github = self.driver.window_handles[-1]
        self.driver.switch_to.window(github)
        assert self.driver.title == 'GitHub - andordavoti/tic-tac-toe-app: Online multiplayer ' \
                                    'Tic Tac Toe game for iOS, android and web.'
        self.driver.close()
    
    @pytest.mark.new_feature
    @pytest.mark.exit_
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

    @pytest.mark.new_tab
    def test_online_game_3(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        button_num_3 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-14lw9ot."
                                                                "r-zmljjp.r-t12b5v.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        button_num_3.click()
        new_game = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                             "r-1otgn73")
        for e in new_game:
            if e.text == "NEW GAME":
                e.click()
        time.sleep(10)
        lobby = self.driver.\
            find_elements_by_css_selector(".css-901oao.r-jwli3a.r-adyw6z.r-vw2c0b")
        lobby = lobby[0].text
        self.driver.execute_script('window.open("https://tictactoe.no/")')
        time.sleep(10)
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        button_num_3 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-14lw9ot."
                                                                "r-zmljjp.r-t12b5v.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        button_num_3.click()
        lobby_id = self.driver.find_element_by_css_selector("input")
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
        assert 3**2 == len(cells) - 5
        self.driver.close()

    @pytest.mark.new_tab
    def test_online_game_4(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        button_num_4 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi."
                                                                "r-gxnn5r.r-17gur6a.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        button_num_4.click()
        new_game = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                             "r-1otgn73")
        for e in new_game:
            if e.text == "NEW GAME":
                e.click()
        time.sleep(10)
        lobby = self.driver.\
            find_elements_by_css_selector(".css-901oao.r-jwli3a.r-adyw6z.r-vw2c0b")
        lobby = lobby[0].text
        self.driver.execute_script('window.open("https://tictactoe.no/")')
        time.sleep(10)
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        button_num_4 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi."
                                                                "r-gxnn5r.r-17gur6a.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        button_num_4.click()
        lobby_id = self.driver.find_element_by_css_selector("input")
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
        assert 4**2 == len(cells) - 5
        self.driver.close()

    @pytest.mark.new_tab
    def test_online_game_5(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        button_num_5 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-pm2fo."
                                                                "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        button_num_5.click()
        new_game = self.driver.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim."
                                                             "r-1otgn73")
        for e in new_game:
            if e.text == "NEW GAME":
                e.click()
        time.sleep(10)
        lobby = self.driver.\
            find_elements_by_css_selector(".css-901oao.r-jwli3a.r-adyw6z.r-vw2c0b")
        lobby = lobby[0].text
        self.driver.execute_script('window.open("https://tictactoe.no/")')
        time.sleep(10)
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        button_num_5 = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-fnzcxi.r-pm2fo."
                                                                "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                                "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                                "r-1mhb1uw")
        button_num_5.click()
        lobby_id = self.driver.find_element_by_css_selector("input")
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
        assert 5**2 == len(cells) - 5
        self.driver.close()
    
    @pytest.mark.new_feature
    @pytest.mark.exit_
    def test_exit_multiplayer(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        exit_button = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-1loqt21."
                                                               "r-18u37iz.r-1mi5vxm.r-fpx60m.r-1otgn73.r-eafdt9."
                                                               "r-1i6wzkk.r-lrvibr")
        exit_button.click()
        header = self.driver.find_element_by_css_selector(".css-4rbku5.css-901oao.css-bfa6kz.r-jwli3a.r-adyw6z")
        assert header.text == "Tic Tac Toe"
    
    @pytest.mark.new_feature
    @pytest.mark.exit_
    def test_exit_online_multiplayer(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "ONLINE MULTIPLAYER":
                e.click()
        exit_button = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-1loqt21."
                                                               "r-18u37iz.r-1mi5vxm.r-fpx60m.r-1otgn73.r-eafdt9."
                                                               "r-1i6wzkk.r-lrvibr")
        exit_button.click()
        header = self.driver.find_element_by_css_selector(".css-4rbku5.css-901oao.css-bfa6kz.r-jwli3a.r-adyw6z")
        assert header.text == "Tic Tac Toe"
    
    @pytest.mark.new_feature
    @pytest.mark.exit_
    def test_exit_settings(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "SETTINGS":
                e.click()
        exit_button = self.driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-1loqt21."
                                                               "r-18u37iz.r-1mi5vxm.r-fpx60m.r-1otgn73.r-eafdt9."
                                                               "r-1i6wzkk.r-lrvibr")
        exit_button.click()
        header = self.driver.find_element_by_css_selector(".css-4rbku5.css-901oao.css-bfa6kz.r-jwli3a.r-adyw6z")
        assert header.text == "Tic Tac Toe"

    @pytest.mark.new_tab
    def test_profile_first(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        profile = self.driver.find_element_by_xpath('//*[contains(text(), "Andor Davoti")]')
        profile.click()
        time.sleep(10)
        github = self.driver.window_handles[-1]
        self.driver.switch_to.window(github)
        assert self.driver.title == 'andordavoti (Andor Davoti) · GitHub'
        self.driver.close()

    @pytest.mark.new_tab
    def test_profile_second(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        profile = self.driver.find_element_by_xpath('//*[contains(text(), "Sanna Jammeh")]')
        profile.click()
        time.sleep(10)
        github = self.driver.window_handles[-1]
        self.driver.switch_to.window(github)
        assert self.driver.title == 'sannajammeh (Sanna Jammeh) · GitHub'
        self.driver.close()

    @pytest.mark.style
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
        hex_color = Color.from_string(background.value_of_css_property("background-color")).hex
        assert hex_color == "#e6eaeb"
    
    @pytest.mark.style    
    def test_change_style_dark(self):
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
        background = self.driver.find_element_by_css_selector(".css-1dbjc4n.r-1awozwy.r-blqegh.r-13awgt0.r-1777fci")
        hex_color = Color.from_string(background.value_of_css_property("background-color")).hex
        assert hex_color == "#2a2d34"

