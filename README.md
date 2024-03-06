# StaffTraveler Automation Project

This project provides an automated solution for JetBlue employees for interacting with available requests on the StaffTraveler website using Python and Selenium. It continuously monitors for new requests and attempts to lock requests in automatically, helping users respond to desired listings more efficiently.

## Prerequisites

- Python 3.8+
- Selenium WebDriver for Chrome if using Chrome versions 114 and prior: https://chromedriver.chromium.org/downloads
  - Not necessary if using Chrome versions 115 and newer
  - NOTE THIS CURRENTLY ONLY WORKS WITH VERSIONS OF CHROME >= 115
  - PREVIOUS BROWSER VERSION SUPPORT TO BE ADDED
- JetBlue Crewmember Active Directory Login with access to ANALYTICS Snowflake database
- Network I.P. configured to access JetBlue's Snowflake database

## Setup

1. **Clone the repository:**
git clone <repository-url>

2. **Install dependencies:**
`pip install -r requirements.txt`

3. **Download and place the WebDriver:**
Place the `chromedriver` in the `./drivers` directory.

## Project Structure

- `/drivers`: WebDrivers (e.g., ChromeDriver)
- `/src`: Source code
- `main.py`: Main script
- `requirements.txt`: Dependencies

## Running the Script

Navigate to the `/src` directory and execute:
`python main.py`

## Contributing

Contributions are welcome! Please fork the project, make your changes, and submit a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This project is for educational purposes only. Ensure compliance with StaffTraveler's terms of service.


## Contributing

Contributions are welcome! Please fork the project, make your changes, and submit a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer

This project is for educational purposes only. Ensure compliance with StaffTraveler's terms of service.


