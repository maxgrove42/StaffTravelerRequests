import sys
import unittest
# Adjust the path below according to your project structure
sys.path.append('../')
from src.snowconn import SnowConn


class TestSnowConn(unittest.TestCase):
    def setUp(self):
        # Set up a SnowConn instance with mocked parameters
        self.snow_conn = SnowConn('mg09329@jetblue.com',
                                  'ANALYST_ROUTE_PLANNING',
                                  'REPORTING_PRD_XS_WH',
                                  'ANALYTICS',
                                  'ANALYTICS',
                                  'jetblue.east-us-2.azure')

    def test_query_flight_for_standby(self):
        # Call the method with test data
        standbySeats = self.snow_conn.queryStandby(569, '2024-03-08')

        # Assert the expected result
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()