# -*- coding: utf-8 -*-
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import re

# Set Chrome options
chrome_options = Options()
# Uncomment the next line if you want to run Chrome in headless mode
chrome_options.add_argument("--headless")

# Initialize WebDriver with ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get('https://stafftraveler.app/requests')

USER_NAME = 'xxx'
PASSWORD = 'xxx'

try:
    wait = WebDriverWait(driver, 30)
    
    #Search for the email field, type in email, and click it.
    wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(USER_NAME)
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
    
    # type in password and send it to log in
    wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(PASSWORD)
    wait.until(EC.element_to_be_clickable((By.ID, "login-with-password"))).click()
    
    while True:  # Continuous monitoring
        # Wait for the elements to be present on the page
        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'chakra-collapse'))
        )
        # print("checking elements")
        for element in elements:
            class_attribute = element.get_attribute('class')
            print(class_attribute)
            # 'css-79elbk' is class of each request
            # 'backdropBlurPolyfill css-1x13gg3' indicates if the request is already taken
            if ("CURRENTLY BEING ANSWERED" not in element.text):
                clickable_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.chakra-collapse')))
                clickable_element.click()
                print("found unclaimed flight")
                #determine the flight information
                #chakra-text css-1m9eb7l = flight num with B6 prepending
                #chakra-text css-1tzeee1 = date

                text = clickable_element.text
                flight_number_match = re.search(r'B6\d+', text)
                date_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}(st|nd|rd|th)?',
                                       text)

                # Clean the date to remove st, nd, rd, th
                cleaned_date = re.sub(r'(st|nd|rd|th)', '', date_match)

                # Current year and current month for comparison
                current_year = datetime.now().year
                current_month = datetime.now().month
                date_obj = datetime.strptime(f"{cleaned_date} {current_year}", "%b %d %Y")

                # If the extracted date is from a month lower than this month,
                # assume the date is for next year.
                if date_obj.month < current_month:
                    date_obj = date_obj.replace(year=current_year + 1)
                    # Format the date as "YYYY-MM-DD"
                formatted_date = date_obj.strftime('%Y-%m-%d')

                print(formatted_date + " on " + flight_number_match)
                seatSpacesToFillIn = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'chakra-numberinput__field css-gal76r'))
                )
                for seatSpace in seatSpacesToFillIn:
                    pass
                    #prepare the seatspaces to be filled in.
                #here we need to click it and claim it.
                #then send it to snowflake to get the seats available.
        # sleep(1)  # Sleep a bit to wait for future requests to come in.
finally:
    driver.quit()
