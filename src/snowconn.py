# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:30:32 2024

@author: MG09329
"""

import snowflake.connector #Used to connect to Snowflake Database
import re
from datetime import datetime


class SnowConn:
    def __init__(self, user, role, warehouse, database, schema, database_url):
        self.conn = snowflake.connector.connect(
                user=user,
                account = database_url,  # Snowflake database website
                role = role,
                warehouse = warehouse,
                database = database,
                schema = schema,
                authenticator = 'externalbrowser',  # authenticate using External Browser for Azure AD
                autocommit = True)

    def __del__(self):
        self.conn.close()
        
    def queryStandby(self, flight_number, flight_date):
        """
        Queries the database for the total non-rev passengers on a flight\n
        
        Parameters:
        - flight_number (int): The flight number to query. Must be an integer.
        - flight_date (str): The start date of the service in 'YYYY-MM-DD' format.
        
        Returns: The number of non-rev pax (integer)
        """
        # Validate flight_number
        if not isinstance(flight_number, int):
            raise ValueError("Flight number must be an integer")
            
        # Validate flight_date format
        if not re.match(r"\d{4}-\d{2}-\d{2}", flight_date):
            raise ValueError("Flight date must be in YYYY-MM-DD format")
        try:
            datetime.strptime(flight_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid flight date provided")
            
        cursor = self.conn.cursor()
        
        # RL1 is myIdTravel agent sign
        query = """select 
                        iff(MARKETING_CLASS_OF_SERVICE IN ('J', 'C', 'D', 'I'), 'J', 'Y') AS CABIN,
                        sum(F.NUMBER_IN_PARTY) as PAX
                    from ANALYTICS.BOOKINGS.FLIGHTS F
                    join ANALYTICS.BOOKINGS.PNR P
                        ON P.PNR_ID = F.PNR_ID
                    where F.MARKETING_AIRLINE_CODE = 'B6'
                       AND F.SERVICE_START_DATE = %s
                       AND F.MARKETING_FLIGHT_NUMBER = %s
                    and p.CREATE_AGENT_SINE = 'RL1'
                    GROUP BY iff(MARKETING_CLASS_OF_SERVICE IN ('J', 'C', 'D', 'I'), 'J', 'Y')
                    """
        
        try:
            # Pass parameters as a tuple to avoid SQL injection
            cursor.execute(query, (flight_date, flight_number))
            result = cursor.fetchone()
            if result[0] is not None:
                return int(result[0])
            else:
                return 0
        finally:
            cursor.close()
