import json
import unittest
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
CHECKDUPLICATES_API_BASE_URL = "https://tkx-qa.liquidanalytix.com/v1/tkxapi/copayEnrollment/checkDuplicates"
CHECKDUPLICATES_AUTHORIZATION_HEADER = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer OHm3JxlDYuhymz5ymUdKmEEp9Zgy'
        }


# Test Cases Class
class InboundTestCases(unittest.TestCase):

    # Test Case 1
    def test_patientMList_api_PING(self):
        print("PINGING Patients API....")

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


    def test_patientMList_api_Throttling(self):
        print("Calling patients api throttling....")

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()

        # parsing the above content which is in string format into json method to convert into json payload
        #payload = json.loads(json_input)

        # Number of requests to send
        num_of_req = 5
        # Time interval between requests (in seconds)
        request_interval = 1  # We can Adjust this based on the API's rate limit

        def send_request():
            try:
                response = requests.post(PATIENTS_API_BASE_URL, data=json_input, headers=PATIENTS_AUTHORIZATION_HEADER)
                json_reponse = json.loads(response.text)
                if response.status_code == 200:
                    print("Request successful")
                else:
                    print(f"Request failed with status code: {response.status_code}")
            except Exception as e:
                print(f"Error: {str(e)}")

        # Send a specified number of requests with a delay
        for i in range(num_of_req):
            send_request()
            time.sleep(request_interval)



    def test_patientMList_api_WithoutAuthorization(self):

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.json', 'r')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 4Ymt8br8rs4JAPIZJZKxYzpff9Zn'
        }

        # reading the content of the body and storing in a variable
        json_input = file.read()

        # parsing the above content which is in string format into json method to convert into json payload
        #request_json = json.loads(json_input)

        # Make a POST request with Json input body
        response = requests.post(PATIENTS_API_BASE_URL, json_input)

        # Asserting to test the status code
        assert response.status_code == 401

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print(json_reponse)

        # Fetch Json path
        errorcode = jsonpath.jsonpath(json_reponse, 'fault')
        err = errorcode[0]['detail']['errorcode']

        # Asserting to test the error description

        self.assertEqual(err, "oauth.v2.InvalidAccessToken")



    def test_patientMList_api_WithAuthorization(self):

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()

        # parsing the above content which is in string format into json method to convert into json payload
        # request_json = json.loads(json_input)

        # Make a POST request with Json input body
        response = requests.post(PATIENTS_API_BASE_URL, json_input, headers = PATIENTS_AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successtext = jsonpath.jsonpath(json_reponse, 'body')

        success = successtext[0]['successDetail']['message']

        # Asserting to test the success description
        self.assertEqual(success, "Patients Request received successfully.")



    def test_patientMList_api_passing_empty_body(self):

        # the json body will be in the file in the specified path
        #file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.json', 'r')

        # reading the content of the body and storing in a variable
        #json_input = file.read()

        # parsing the above content which is in string format into json method to convert into json payload
        # request_json = json.loads(json_input)

        # Make a POST request with Json input body
        response = requests.post(PATIENTS_API_BASE_URL, headers = PATIENTS_AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 400

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print(json_reponse)

        # Fetch Json path
        errorstatus = jsonpath.jsonpath(json_reponse, 'status')[0]
        errorMessage = jsonpath.jsonpath(json_reponse, 'errorMessage')

        error_message_list = ['Error validating JSON.', 'expected type: JSONObject, found: Null']
        # Asserting to test the success description
        self.assertEqual(errorstatus, "Failure - Bad Request")
        self.assertEqual(errorMessage[0], error_message_list)


    def test_patientMList_api_passing_xml_body(self):

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.xml', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()

        # Make a POST request with Json input body
        response = requests.post(PATIENTS_API_BASE_URL, json_input, headers = PATIENTS_AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 400

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print(json_reponse)

        # Fetch Json path
        errortext = jsonpath.jsonpath(json_reponse, 'errorMessage')
        error = errortext[0][0]

        # Asserting to test the success description
        self.assertEqual(error, "Error validating JSON.")



    def test_patientMList_api_with_get_method(self):

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()

        # Getting response of URL
        response = requests.get(PATIENTS_API_BASE_URL,data=json_input,headers=PATIENTS_AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print(json_reponse)

        # Fetch Json path
        errorStatus = jsonpath.jsonpath(json_reponse,'status')[0]
        errorMessage = jsonpath.jsonpath(json_reponse, 'errorMessage')[0][0]

        self.assertEqual(errorStatus, "Failure - Resource not found")
        self.assertEqual(errorMessage, "Please check the Resource Path or HTTP Method.")


    def test_patientMList_api_with_put_method(self):

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()
        response = requests.put(PATIENTS_API_BASE_URL,data=json_input,headers=PATIENTS_AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        errorStatus = jsonpath.jsonpath(json_reponse, 'status')[0]
        errorMessage = jsonpath.jsonpath(json_reponse, 'errorMessage')[0][0]

        self.assertEqual(errorStatus, "Failure - Resource not found")
        self.assertEqual(errorMessage, "Please check the Resource Path or HTTP Method.")


    def test_patientMList_api_with_patch_method(self):

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()
        response = requests.patch(PATIENTS_API_BASE_URL,data=json_input,headers=PATIENTS_AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        errorStatus = jsonpath.jsonpath(json_reponse, 'status')[0]
        errorMessage = jsonpath.jsonpath(json_reponse, 'errorMessage')[0][0]

        self.assertEqual(errorStatus, "Failure - Resource not found")
        self.assertEqual(errorMessage, "Please check the Resource Path or HTTP Method.")


    def test_patientMList_api_with_delete_method(self):

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\patientTestData.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()
        response = requests.delete(PATIENTS_API_BASE_URL,data=json_input,headers=PATIENTS_AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        errorStatus = jsonpath.jsonpath(json_reponse, 'status')[0]
        errorMessage = jsonpath.jsonpath(json_reponse, 'errorMessage')[0][0]

        self.assertEqual(errorStatus, "Failure - Resource not found")
        self.assertEqual(errorMessage, "Please check the Resource Path or HTTP Method.")


    def test_checkDuplicates_api_recNotFoundScenario(self):

        # the json body will be in the file in the specified path
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\CheckDuplicatesTestDataRecNotFound.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()
        start_time = time.time()

        # Make a POST request with Json input body
        response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER)
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
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\CheckDuplicatesTestDataRecFound.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()
        start_time = time.time()

        # Make a POST request with Json input body
        response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER)
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
        file = open('C:\\Users\\pekabath\\PycharmProjects\\API Data\\CheckDuplicatesTestDataMissingField.json', 'r')

        # reading the content of the body and storing in a variable
        json_input = file.read()
        start_time = time.time()

        # Make a POST request with Json input body
        response = requests.post(CHECKDUPLICATES_API_BASE_URL, json_input, headers = CHECKDUPLICATES_AUTHORIZATION_HEADER)
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



