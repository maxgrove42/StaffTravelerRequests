from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class MyIdTravelConn:
    myIdSite = 'https://www.myidtravel.com/'
    airline = 'JetBlue'

    def __init__(self, user, pwd):
        self.__start_id_site()
        self.__login(user, pwd)

    def __start_id_site(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")  # bypass OS security model
        chrome_options.add_argument('--remote-debugging-port=9222')  # for visualization in chrome dev
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),
                                       options=chrome_options)
        self.driver.get(MyIdTravelConn.myIdSite)

    def __login(self, user, pwd):
        self.wait = WebDriverWait(self.driver, 120)

        # Search for the email field, type in email, and click it.
        (self.wait.until(EC.element_to_be_clickable((By.ID, "input-airline")))
         .send_keys(MyIdTravelConn.airline, Keys.ENTER))

        self.wait.until(EC.element_to_be_clickable((By.ID, "user"))).send_keys(user)
        self.wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(pwd)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "loginButton"))).click()  # login
        self.wait.until(EC.element_to_be_clickable((By.ID, 'checkbox-1041'))).click()  # privacy checkbox
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button-1042'))).click()  # confirm privacy

    def find_seats(self, orig, dest, flight_date, flight_num):

        self.wait.until(EC.element_to_be_clickable(
            (By.ID, 'bookingandlistingbutton-1026-btnInnerEl'))).click()  # navigate to new flight

        # select first traveler
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "[id^='booking-travellerselection-registeredtraveller-']"))).click()

        self.__click_continue()

        # type in origin, dest, and dat
        self.wait.until(EC.element_to_be_clickable((By.NAME, 'origin'))).send_keys(orig, Keys.TAB,  # send orig
                                                                                   dest, Keys.TAB,  # send dest
                                                                                   flight_date, Keys.TAB, # send date
                                                                                   Keys.TAB, Keys.TAB, Keys.TAB,
                                                                                   Keys.ENTER)  #navigate to continue

        #now we just need to select the right flight, get the seats and report out.

        flights = self.wait.until(EC.presence_of_all_elements_located(By.CLASS_NAME,
                                                                      'x-container-default'))

    def __click_continue(self):
        navigation_buttons_container = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".x-container.navigation-buttons.x-container-default.x-box-layout-ct")))

        # Find all elements within this container that can act as buttons
        buttons = navigation_buttons_container.find_elements(By.CSS_SELECTOR, "[role='button']")

        # Iterate through the buttons to find the first one with aria-hidden="false"
        for button in buttons:
            if button.get_attribute("aria-hidden") == "false":
                button.click()  # Click the first button meeting the condition
                break  # Exit the loop after clicking the desired button


myVar = MyIdTravelConn('xxxxx', 'xxxxx')
myVar.find_seats('jfk', 'mco', '2024-03-08', '569')
