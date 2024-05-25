"""This file runs the ET Hangman game."""

# Modules and libraries
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets API setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Authorization for Google Sheets API
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open world countries sheet
COUNTRIES_SHEET = GSPREAD_CLIENT.open("world_countries").sheet1


# Function to get countries from Google Sheet
def get_countries(sheet):
    """
    Get list of countries
    """
    return sheet.col_values(1)


# Function to validate a country
def validate_country(country_name, country_list):
    """
    Validate the country names against the list of countries
    """
    return country_name.upper() in [country.upper() for country in country_list]


# Run test
def main():
    countries = get_countries(COUNTRIES_SHEET)
    print("Fetched conuntries list from Google Sheet.")

    " Test countries"
    test_countries = ["Sweden", "Norway", "InvalidCountry"]

    for country in test_countries:
        if validate_country(country, countries):
            print(f"{country} is a valid country.")
        else:
            print(f"{country} is not a valid country.")


if __name__ == "__main__":
    main()
