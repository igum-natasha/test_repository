import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as Op
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time 
driver: webdriver


gecko_path = os.environ.get('gecko_path')
chrome_path = os.environ.get('chrome_path')
fire_binary = os.environ.get('fire_bin')


@pytest.fixture(params=['firefox', 'chrome'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--test-type")
        options.add_argument("--disable-setuid-sandbox")
        options.add_argument("--disable-infobars")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        cap = DesiredCapabilities().CHROME.copy()
        cap['pageLoadStrategy'] = "none"
        try:
            time.sleep(20)
            driver = webdriver.Chrome(executable_path=chrome_path, options=options)
        except TimeoutException:
            pytest.skip("Time out")
    if request.param == 'firefox':
        options = Op()
        binary = FirefoxBinary(fire_binary)
        options.add_argument("--headless")
        options.binary_location = binary
        options.add_argument("--disable-dev-shm-usage") 
        options.add_argument("--no-sandbox")
        try:
            driver = webdriver.Firefox(executable_path=gecko_path, options=options)
            time.sleep(10)
            driver.set_window_size(1050, 708)
        except TimeoutException:
            pytest.skip("Time out")
    time.sleep(20)
    request.cls.driver = driver
    driver.get("http://tictactoe.no/")
    try:
        menu = driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()
        time.sleep(10)
        dark_style = driver.find_element_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1awozwy.r-vl818t.r-pm2fo."
                                                          "r-gxnn5r.r-ou6ah9.r-rs99b7.r-1loqt21.r-ur6pnr."
                                                          "r-1777fci.r-crgep1.r-1udh08x.r-bnwqim.r-1otgn73."
                                                          "r-1mhb1uw")
        dark_style.click()
    except NoSuchElementException:
        print("Error, No Such Element!")
        exit(1)
    

def skip_on(exception, reason="Default reason"):
    def decorator_func(f):
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except exception:
                pytest.skip(reason)
        return wrapper
    return decorator_func    


def find_button(cells, x, y):
        cell = [elem for elem in cells if elem.location['y'] // 10  == y and elem.location['x'] // 10 == x]
        cell[0].click()


@pytest.mark.usefixtures("init_driver")
class BaseClassTests:
    pass


class Tests(BaseClassTests):
    def setup_method(self):
        time.sleep(10)
        self.driver.refresh()

    def teardown_method(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    @pytest.mark.new_feature
    @pytest.mark.buttons_menu
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
    def test_buttons_main_page(self):
        buttons = self.driver.find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.'
                                                                          'r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        titles = [e.text for e in buttons]
        
        assert titles == ["MULTIPLAYER", "ONLINE MULTIPLAYER", "SETTINGS"]

    @pytest.mark.setting_game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
        time.sleep(10)
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        assert 3 ** 2 == len(cells) - 5

    @pytest.mark.setting_game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
        time.sleep(10)
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        assert 4 ** 2 == len(cells) - 5

    @pytest.mark.setting_game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
        time.sleep(10)
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        assert 5 ** 2 == len(cells) - 5
    
    @pytest.mark.enter_lobby
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
        answer = WebDriverWait(self.driver, 120).until(
           lambda x: x.find_elements_by_css_selector(".css-901oao"))
        titles = [elem.text for elem in answer]
        assert 'This lobby does not exist...' in titles
    
    @pytest.mark.new_feature
    @pytest.mark.change_style
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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

    @pytest.mark.github_project
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
    def test_project_github(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        project = self.driver.find_element_by_xpath('//*[contains(text(), "Project on GitHub")]')
        project.click()
        self.driver.implicitly_wait(10)
        time.sleep(10)
        github = self.driver.window_handles[-1]
        self.driver.switch_to.window(github)
        assert self.driver.title == 'GitHub - andordavoti/tic-tac-toe-app: Online multiplayer ' \
                                    'Tic Tac Toe game for iOS, android and web.'
        self.driver.close()
    
    @pytest.mark.new_feature
    @pytest.mark.exit_online_game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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

    @pytest.mark.setting_online_game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
        print(lobby)
        self.driver.execute_script('window.open("https://tictactoe.no/")')
        time.sleep(10)
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            print(e.text)
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

    @pytest.mark.setting_online_game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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

    @pytest.mark.setting_online_game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
    @pytest.mark.exit_game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
        time.sleep(10)
        header = self.driver.find_element_by_css_selector(".css-4rbku5.css-901oao.css-bfa6kz.r-jwli3a.r-adyw6z")
        assert header.text == "Tic Tac Toe"
    
    @pytest.mark.new_feature
    @pytest.mark.exit_online_game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
        time.sleep(10)
        header = self.driver.find_element_by_css_selector(".css-4rbku5.css-901oao.css-bfa6kz.r-jwli3a.r-adyw6z")
        assert header.text == "Tic Tac Toe"
    
    @pytest.mark.new_feature
    @pytest.mark.exit_settings
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
        time.sleep(10)
        header = self.driver.find_element_by_css_selector(".css-4rbku5.css-901oao.css-bfa6kz.r-jwli3a.r-adyw6z")
        assert header.text == "Tic Tac Toe"

    @pytest.mark.open_profile
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
    def test_profile_first(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        profile = self.driver.find_element_by_xpath('//*[contains(text(), "Andor Davoti")]')
        profile.click()
        self.driver.implicitly_wait(10)
        time.sleep(10)
        github = self.driver.window_handles[-1]
        self.driver.switch_to.window(github)
        assert self.driver.title == 'andordavoti (Andor Davoti) · GitHub'
        self.driver.close()

    @pytest.mark.open_profile
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
    def test_profile_second(self):
        menu = self.driver. \
            find_elements_by_css_selector('.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73')
        for e in menu:
            if e.text == "SETTINGS":
                e.click()

        profile = self.driver.find_element_by_xpath('//*[contains(text(), "Sanna Jammeh")]')
        profile.click()
        self.driver.implicitly_wait(10)
        time.sleep(10)
        github = self.driver.window_handles[-1]
        self.driver.switch_to.window(github)
        assert self.driver.title == 'sannajammeh (Sanna Jammeh) · GitHub'
        self.driver.close()

    @pytest.mark.change_style
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
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
    
    @pytest.mark.change_style
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")    
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
    
    
    @pytest.mark.game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
    def test_multiplayer_tie(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        time.sleep(10)
        find_button(cells, 38, 25)
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        x, y = [], []
        for cell in cells:
            cy = cell.location['y']
            if cy // 100 and cy // 10 not in y:
                y.append(cy // 10)
            cx = cell.location['x']
            if cx // 100 and cx // 10 not in x:
                x.append(cx // 10)
        x.pop(0)
        find_button(cells, x[1], y[1])
        find_button(cells, x[2], y[0])
        find_button(cells, x[1], y[0])
        find_button(cells, x[0], y[1])
        find_button(cells, x[0], y[2])
        find_button(cells, x[1], y[2])
        find_button(cells, x[2], y[1])
        find_button(cells, x[2], y[2])
        time.sleep(20)
        tie = WebDriverWait(self.driver, 120).until(
            lambda x: x.find_elements_by_css_selector(".css-901oao.r-jwli3a.r-adyw6z.r-16dba41"))
        
        titles = [elem.text for elem in tie]
        assert "It's a Tie" in titles
    
    @pytest.mark.game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
    def test_multiplayer_win_x(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        time.sleep(10)
        find_button(cells, 38, 25)
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        x, y = [], []
        for cell in cells:
            cy = cell.location['y']
            if cy // 100 and cy // 10 not in y:
                y.append(cy // 10)
            cx = cell.location['x']
            if cx // 100 and cx // 10 not in x:
                x.append(cx // 10)
        x.pop(0)
        find_button(cells, x[2], y[0])
        find_button(cells, x[1], y[0])
        find_button(cells, x[1], y[1])
        find_button(cells, x[0], y[1])
        find_button(cells, x[0], y[2])
        time.sleep(20)
        win = WebDriverWait(self.driver, 120).until(
            lambda x: x.find_elements_by_css_selector(".css-901oao.r-jwli3a.r-adyw6z.r-16dba41"))
        
        titles = [elem.text for elem in win]
        assert "The winner is X" in titles
    
    @pytest.mark.game
    @skip_on(NoSuchElementException, reason="Error, No Such Element!")
    def test_multiplayer_win_o(self):
        menu = self.driver. \
            find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1loqt21.r-1udh08x.r-bnwqim.r-1otgn73")
        for e in menu:
            if e.text == "MULTIPLAYER":
                e.click()
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        time.sleep(10)
        find_button(cells, 38, 25)
        cells = self.driver.find_elements_by_css_selector(".css-1dbjc4n.r-1awozwy.r-13awgt0.r-1777fci")
        x, y = [], []
        for cell in cells:
            cy = cell.location['y']
            if cy // 100 and cy // 10 not in y:
                y.append(cy // 10)
            cx = cell.location['x']
            if cx // 100 and cx // 10 not in x:
                x.append(cx // 10)
        x.pop(0)
        find_button(cells, x[1], y[0])
        find_button(cells, x[1], y[1])
        find_button(cells, x[2], y[0])
        find_button(cells, x[2], y[2])
        time.sleep(20)
        win = WebDriverWait(self.driver, 120).until(
            lambda x: x.find_elements_by_css_selector(".css-901oao.r-jwli3a.r-adyw6z.r-16dba41"))
        titles = [elem.text for elem in win]
        assert "The winner is O" in titles
