# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get('https://stafftraveler.app/requests')

USER_NAME = 'max.grove@jetblue.com'
PASSWORD = 'Routeplan2023*'

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
        
        for element in elements:
            class_attribute = element.get_attribute('class')
            
            # 'css-79elbk' is class of each request
            # 'backdropBlurPolyfill css-1x13gg3' indicates if the request is already taken
            if 'css-79elbk' in class_attribute and 'backdropBlurPolyfill css-1x13gg3' not in class_attribute:
                EC.element_to_be_clickable((By.CLASS, "css-79elbk")).click()
                
                #determine the flight information
                #chakra-text css-1m9eb7l = flight num with B6 prepending
                #chakra-text css-1tzeee1 = date
                flightNumber = driver.find_element_by_class_name('chakra-text css-1m9eb7l').text
                flightDate = driver.find_element_by_class_name('chakra-text css-1tzeee1').text
    
                seatSpacesToFillIn = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'chakra-numberinput__field css-gal76r'))
                )
                for seatSpace in seatSpacesToFillIn:
                    pass
                    #prepare the seatspaces to be filled in.
                #here we need to click it and claim it.
                #then send it to snowflake to get the seats available.
        sleep(5)  # Sleep a bit to wait for future requests to come in.
finally:
    driver.quit()