from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class MyIdTravelConn:
    myIdSite = 'https://www.myidtravel.com/'
    airline = 'JetBlue'

    def __init__(self, user, pwd, flight_num, flight_date):
        self.user = user
        self.pwd = pwd
        self.flight_num = flight_num
        self.flight_date = flight_date
        self.__startWebDriver()

    def __startWebDriver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")  # bypass OS security model
        chrome_options.add_argument('--remote-debugging-port=9222')  # for visualization in chrome dev
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),
                                       options=chrome_options)
        self.driver.get(MyIdTravelConn.myIdSite)
        wait = WebDriverWait(self.driver, 120)

        # Search for the email field, type in email, and click it.
        wait.until(EC.element_to_be_clickable((By.ID, "input-airline"))).send_keys(MyIdTravelConn.airline)
        wait.until(EC.element_to_be_clickable((By.ID, "user"))).send_keys(self.user)
        wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(self.pwd)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "loginButton"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'checkbox-1041'))).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'button-1042'))).click()


# myVar = MyIdTravelConn('xxx', 'xxx', 'xxx', flight_date='yyyy-mm-dd')

