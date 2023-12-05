import unittest
import json
import jsonpath
import time
import requests

# Exception Class
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Configuration
PATIENTS_API_BASE_URL = "https://tkx-qa.liquidanalytix.com/v1/tkxapi/patients"
PATIENTS_AUTHORIZATION_HEADER = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 4Ymt8br8rs4JAPIZJZKxYzpff9Zn'
        }

# Test Cases Class
class APISampleTestCaseScript(unittest.TestCase):

    # Test Case 1
    def test_patientMList_api_PING(self):
        print("PINGING Patients API to check sample test....")

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()
        start_time = time.time()
        response = requests.post(PATIENTS_API_BASE_URL, data=json_input, headers=PATIENTS_AUTHORIZATION_HEADER)
        end_time = time.time()
        try:
            if response.status_code != 200:
                raise CustomError(f"Patients API is NOT reachable. Status code: {response.status_code}")
            elapsed_time = end_time - start_time
            print(f"Patients API is reachable. Response time: {elapsed_time:.2f} seconds")
        except CustomError as e:
            print(f"Error While pinging Patients API:\n {e}")


if __name__ == '__main__':
    unittest.main()
