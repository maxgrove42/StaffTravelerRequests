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
        self.wait.until(EC.element_to_be_clickable((By.ID, "input-airline"))).send_keys(MyIdTravelConn.airline)
        self.wait.until(EC.element_to_be_clickable((By.ID, "user"))).send_keys(user)
        self.wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(pwd)
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "loginButton"))).click() #login
        self. wait.until(EC.element_to_be_clickable((By.ID, 'checkbox-1041'))).click() #privacy checkbox
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button-1042'))).click() #confirm privacy

    def find_seats(self, orig, dest, flight_date, flight_num):

        self.wait.until(EC.element_to_be_clickable((By.ID, 'bookingandlistingbutton-1026-btnInnerEl'))).click() #navigate to new flight

        # this line is giving problems
        self.wait.until(EC.element_to_be_clickable((By.ID, 'booking-travellerselection-registeredtraveller-1072'))).click() #select primary traveler
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button-1257-btnInnerEl'))).click() #click continue
        self.wait.until(EC.element_to_be_clickable((By.ID, 'airportautocomplete-1332-inputEl'))).send_keys(orig) #send orig
        self.wait.until(EC.element_to_be_clickable((By.ID, 'airportautocomplete-1334-inputEl'))).send_keys(dest) #send dest
        self.wait.until(EC.element_to_be_clickable((By.ID, 'myiddatefield-field-1339-inputEl'))).send_keys(flight_date) #load flight date. myidtravel handles format conversio
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button-1346-btnInnerEl'))).click() #click continue
        flights = self.wait.until(EC.presence_of_all_elements_located(By.CLASS_NAME,
                                                                 'x-container-default'))

myVar = MyIdTravelConn('xxx', 'xxx')
myVar.find_seats('jfk', 'mco', '2024-03-08', '569')
