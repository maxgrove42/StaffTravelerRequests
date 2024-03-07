# -*- coding: utf-8 -*-
from datetime import datetime
from selenium.common.exceptions import TimeoutException
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
chrome_options.add_argument("--no-sandbox")  # bypass OS security model
chrome_options.add_argument('--remote-debugging-port=9222') # Recommended is 9222

# Initialize WebDriver with ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(),
                          options=chrome_options)


driver.get('https://stafftraveler.app/requests')

USER_NAME = 'XXXXX'
PASSWORD = 'XXXX'

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

        # Step 1: Find the first 'css-0' container
        first_css_0_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-0'))
        )

        # Step 2: Find all 'css-79elbk' elements within this container
        css_79elbk_elements = first_css_0_container.find_elements(By.CLASS_NAME, 'css-79elbk')

        valid_elements = []  # To store elements that pass your criteria
        for element in css_79elbk_elements:
            # Check if the element does not have any child with the class 'css-a6bwly'
            if not element.find_elements(By.CLASS_NAME, 'css-a6bwly'):
                valid_elements.append(element)

        # print("checking elements")
        for element in valid_elements:
            clickable_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.css-79elbk')))
            clickable_element.click()
            print("found unclaimed flight")
            #determine the flight information
            #chakra-text css-1m9eb7l = flight num with B6 prepending
            #chakra-text css-1tzeee1 = date

            text = clickable_element.text
            flight_number_match = re.search(r'B6\d+', text)

            if flight_number_match:
                cleaned_flight_number = flight_number_match.group()
            else:
                print('Error in flight number matching, proceeding to next flight')
                continue

            date_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2}(st|nd|rd|th)?',
                                   text)
            if date_match:
                cleaned_date = re.sub(r'(st|nd|rd|th)', '', date_match.group())
            else:
                # Handle the case where there was no match
                print('Error in date matching, proceeding to next flight')
                continue

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

            print(formatted_date + " on " + cleaned_flight_number)
            seatSpacesToFillIn = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-gal76r'))
            )

            #first, business, eco+, eco, nonrev
            seatSpaceResponses = [0, 5, 0, 1, 26] #dummy values for now, will need to pull from MyIdTravel eventually

            for (seatSpace, response) in zip(seatSpacesToFillIn, seatSpaceResponses):
                seatSpace.clear()  # Clear any pre-filled value
                seatSpace.send_keys(str(response))
                sleep(1)

            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "css-yvwpf5"))).click()
            #click again if we are prompted to do so in case of what StaffTraveler deems suspicious loads.
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-yvwpf5"))).click()
            except TimeoutException:
                print("No need for second click.")
        sleep(0.5)  # Sleep a bit to wait for future requests to come in.
finally:
    driver.quit()
