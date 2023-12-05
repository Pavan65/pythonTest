import json
import unittest
import jsonpath
import time
import requests
import configparser

# Load configuration from the file
config = configparser.ConfigParser()
config.read('config.ini')

# Choose the environment here (DEV or PROD)
environment = "COPAY_DEV"

# Get the environment from the command line argument or environment variable
#self.environment = sys.argv[1].upper() if len(sys.argv) > 1 else "DEV"

# Use the specified environment to get the base URLs
#self.CREATECOPAYENROLLMENT_API_BASE_URL = config[self.environment]['CREATECOPAYENROLLMENT_API_BASE_URL']

# Configuration
CHECKDUPLICATES_API_BASE_URL = config[environment]['CHECKDUPLICATES_API_BASE_URL']
CHECKDUPLICATES_AUTHORIZATION_HEADER = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer OHm3JxlDYuhymz5ymUdKmEEp9Zgy'
        }

CHECKDUPLICATES_AUTHORIZATION_HEADER1 = {
            'Content-Type': 'application/json'
        }


# Test Cases Class
class CheckDUplicatesTestCase(unittest.TestCase):
    def test_checkDuplicates_api_recNotFoundScenario(self):

        # the json body will be in the file in the specified path
        with open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\CheckDuplicatesTestDataRecNotFound.json', 'r') as file:
            # reading the content of the body and storing in a variable
            json_input = file.read()

        start_time = time.time()

        # Make a POST request with Json input body
        if environment == "COPAY_DEV":
            response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER1)
        elif environment == "COPAY_QA":
            response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER)
        elif environment == "COPAY_PROD":
            response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER)
        else:
            print("Check Duplicates API error :\nEnvironment was not chosen properly")

        end_time = time.time()

        # Asserting to test the status code
        assert response.status_code == 200
        elapsed_time = end_time - start_time

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successtext = jsonpath.jsonpath(json_reponse, 'patientRecordResp')

        success = successtext[0]['statusDesc']

        # Asserting to test the success description
        self.assertEqual(success, "Matching record not found")
        print(f"CheckDuplicates API is reachable with test record Not found scenario. Response time: {elapsed_time:.2f} seconds")


    def test_checkDuplicates_api_recFoundScenario(self):

        # the json body will be in the file in the specified path
        with open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\CheckDuplicatesTestDataRecFound.json', 'r') as file:
            # reading the content of the body and storing in a variable
            json_input = file.read()

        start_time = time.time()

        # Make a POST request with Json input body
        if environment == "COPAY_DEV":
            response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER1)
        elif environment == "COPAY_QA":
            response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER)
        elif environment == "COPAY_PROD":
            response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER)
        else:
            print("Check Duplicates API error :\nEnvironment was not chosen properly")

        end_time = time.time()

        # Asserting to test the status code
        assert response.status_code == 200
        elapsed_time = end_time - start_time

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successtext = jsonpath.jsonpath(json_reponse, 'patientRecordResp')

        success = successtext[0]['statusDesc']

        # Asserting to test the success description
        self.assertEqual(success, "Matching record found")
        print(f"CheckDuplicates API is reachable with test record found scenario. Response time: {elapsed_time:.2f} seconds")


    def test_checkDuplicates_api_missingFieldScenario(self):

        # the json body will be in the file in the specified path
        with open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\CheckDuplicatesTestDataMissingField.json', 'r') as file:
            # reading the content of the body and storing in a variable
            json_input = file.read()

        start_time = time.time()

        # Make a POST request with Json input body
        if environment == "COPAY_DEV":
            response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER1)
        elif environment == "COPAY_QA":
            response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER)
        elif environment == "COPAY_PROD":
            response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER)
        else:
            print("Check Duplicates API error :\nEnvironment was not chosen properly")

        end_time = time.time()

        # Asserting to test the status code
        assert response.status_code == 400
        elapsed_time = end_time - start_time

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print(json_reponse)

        # Fetch Json path
        errorMessage = jsonpath.jsonpath(json_reponse, 'errorMessage')[0]
        errorDescription = jsonpath.jsonpath(json_reponse, 'errorDescription')[0]

        # Asserting to test the error description
        self.assertEqual(errorMessage, "Bad request")
        self.assertEqual(errorDescription, "Patient first name, patient last name, date of birth, gender, city, state and zipcode are mandatory")
        print(f"CheckDuplicates API is reachable with test missing field scenario. Response time: {elapsed_time:.2f} seconds")


if __name__ == '__main__':
    unittest.main()

