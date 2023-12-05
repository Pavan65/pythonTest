import requests
import json
import jsonpath
import unittest
import time
from requests.auth import HTTPBasicAuth

# Exception Class
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Configuration
SPSTATUS_API_BASE_URL = "https://tkx-qa.liquidanalytix.com/v1/tkxapi/spstatus"
DISPENSE_API_BASE_URL = "https://tkx-qa.liquidanalytix.com/v1/tkxapi/dispense"
AUTHORIZATION_HEADER = {
            'Accept': 'application/json',
            'Authorization': 'Bearer 4Ymt8br8rs4JAPIZJZKxYzpff9Zn'
        }

# Test Cases Class
class ExtractsTestCase(unittest.TestCase):


    def test_spStatus_api_PING(self):
        print("PINGING SP Status API....")
        start_time = time.time()
        response = requests.request("GET", SPSTATUS_API_BASE_URL, headers = AUTHORIZATION_HEADER)
        end_time = time.time()
        try:
            if response.status_code != 200:
                raise CustomError(f"Status API is NOT reachable. Status code: {response.status_code}")
            elapsed_time = end_time - start_time
            print(f"Status API is reachable. Response time: {elapsed_time:.2f} seconds")
        except CustomError as e:
            print(f"Error While pinging status API:\n {e}")


    def test_dispense_api_PING(self):
        print("PINGING Dispense API....")
        start_time = time.time()
        response = requests.request("GET", DISPENSE_API_BASE_URL, headers = AUTHORIZATION_HEADER)
        end_time = time.time()
        try:
            if response.status_code != 200:
                raise CustomError(f"Dispense API is NOT reachable. Status code: {response.status_code}")
            elapsed_time = end_time - start_time
            print(f"Dispense API is reachable. Response time: {elapsed_time:.2f} seconds")
        except CustomError as e:
            print(f"Error While pinging Dispense API:\n {e}")


    def test_spStatus_api_Throttling(self):
        print("Calling sp status api throttling....")
        # Number of requests to send
        num_of_req = 5
        # Time interval between requests (in seconds)
        request_interval = 1  # We can Adjust this based on the API's rate limit

        def send_request():
            try:
                response = requests.get(SPSTATUS_API_BASE_URL, headers=AUTHORIZATION_HEADER)
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


    def test_dispense_api_Throttling(self):
        print("Calling dispense api throttling....")
        # Number of requests to send
        num_of_req = 5
        # Time interval between requests (in seconds)
        request_interval = 1  # We can Adjust this based on the API's rate limit

        def send_request():
            try:
                response = requests.get(DISPENSE_API_BASE_URL, headers=AUTHORIZATION_HEADER)
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


    def test_spStatus_api_without_AuthorizationToken(self):

        # Getting response of URL
        response = requests.get(SPSTATUS_API_BASE_URL)
        #print("\nThe response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 401

        # Displaying response content/body
        #print("\nThe content is: \n", response.content)

        # Displaying the response headers/errors
        #print("\nThe response headers are: \n", response.headers)

        # If we want to print the 'WWW-Authenticate' from headers
        #print("\n the response of Authenticate in headers is : \n", response.headers.get('WWW-Authenticate'))

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)


        # Fetch Json path
        errorcode = jsonpath.jsonpath(json_reponse,'fault')
        #print("\nthe error code :\n", errorcode)
        err = errorcode[0]['detail']['errorcode']
        #print("\nThe json path/error code is: \n", err)

        self.assertEqual(err, "oauth.v2.InvalidAccessToken")



    def test_dispense_api_without_AuthorizationToken(self):

        # Getting response of URL
        response = requests.get(DISPENSE_API_BASE_URL)
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 401

        # Displaying response content/body
        #print("\nThe content is: \n", response.content)

        # Displaying the response headers/errors
        #print("\nThe response headers are: \n", response.headers)

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        errorcode = jsonpath.jsonpath(json_reponse,'fault')
        #print("\nthe error code :\n", errorcode)
        err = errorcode[0]['detail']['errorcode']
        #print("\nThe json path/error code is: \n", err)

        self.assertEqual(err, "oauth.v2.InvalidAccessToken")



    def test_spStatus_api_with_AuthorizationToken(self):

        # Getting response of URL
        response = requests.request("GET", SPSTATUS_API_BASE_URL, headers = AUTHORIZATION_HEADER)

        #if we want to use Basic auth then below is the code
        #response = requests.request("GET", url, headers=headers, auth=HTTPBasicAuth(username="username", password="password"))
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        successDetails = jsonpath.jsonpath(json_reponse,'body')
        #print("\nthe success details :\n", successDetails)
        success = successDetails[0]['successDetail']['message']
        #print("\nThe json path/success code is: \n", success)

        self.assertEqual(success, "Status data is being posted to Takeda")



    def test_dispense_api_with_AuthorizationToken(self):

        # Getting response of URL
        response = requests.request("GET", DISPENSE_API_BASE_URL, headers = AUTHORIZATION_HEADER)

        #if we want to use Basic auth then below is the code
        #response = requests.request("GET", url, headers=headers, auth=HTTPBasicAuth(username="username", password="password"))
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        successDetails = jsonpath.jsonpath(json_reponse,'body')
        #print("\nthe success details :\n", successDetails)
        success = successDetails[0]['successDetail']['message']
        #print("\nThe json path/success code is: \n", success)

        self.assertEqual(success, "Dispense data is being posted to Takeda")


    def test_spStatus_api_with_post_method(self):

        payload = {}
        # Getting response of URL
        response = requests.request("POST", SPSTATUS_API_BASE_URL, headers = AUTHORIZATION_HEADER)

        #if we want to use Basic auth then below is the code
        #response = requests.request("POST", SPSTATUS_API_BASE_URL, headers=AUTHORIZATION_HEADER, data= payload,auth=HTTPBasicAuth(username="username", password="password"))
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        FailureResponse = jsonpath.jsonpath(json_reponse,'status')
        #print("\nthe success details :\n", FailureResponse)
        failure = FailureResponse[0]
        #print("\nThe json path/success code is: \n", failure)

        self.assertEqual(failure, "Failure - Resource not found")



    def test_dispense_api_with_post_method(self):

        payload = {}
        # Getting response of URL
        response = requests.request("POST", DISPENSE_API_BASE_URL, headers = AUTHORIZATION_HEADER)

        #if we want to use Basic auth then below is the code
        #response = requests.request("POST", DISPENSE_API_BASE_URL, headers=AUTHORIZATION_HEADER, data= payload, auth=HTTPBasicAuth(username="username", password="password"))
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        FailureResponse = jsonpath.jsonpath(json_reponse,'status')
        #print("\nthe success details :\n", FailureResponse)
        failure = FailureResponse[0]
        #print("\nThe json path/success code is: \n", failure)

        self.assertEqual(failure, "Failure - Resource not found")


    def test_spStatus_api_with_put_method(self):

        payload = {}
        # Getting response of URL
        #response = requests.request("POST", url, headers = headers)

        #if we want to use Basic auth then below is the code
        #response = requests.request("POST", url, headers=headers, data= payload,auth=HTTPBasicAuth(username="username", password="password"))
        response = requests.put(SPSTATUS_API_BASE_URL,data=payload,headers=AUTHORIZATION_HEADER)
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        FailureResponse = jsonpath.jsonpath(json_reponse,'status')
        #print("\nthe success details :\n", FailureResponse)
        failure = FailureResponse[0]
        #print("\nThe json path/success code is: \n", failure)

        self.assertEqual(failure, "Failure - Resource not found")


    def test_dispense_api_with_put_method(self):

        payload = {}
        # Getting response of URL
        #response = requests.request("POST", url, headers = headers)

        #if we want to use Basic auth then below is the code
        #response = requests.request("POST", url, headers=headers, data= payload, auth=HTTPBasicAuth(username="username", password="password"))
        response = requests.put(DISPENSE_API_BASE_URL, data=payload, headers=AUTHORIZATION_HEADER)
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        FailureResponse = jsonpath.jsonpath(json_reponse,'status')
        #print("\nthe success details :\n", FailureResponse)
        failure = FailureResponse[0]
        #print("\nThe json path/success code is: \n", failure)

        self.assertEqual(failure, "Failure - Resource not found")


    def test_spStatus_api_with_patch_method(self):

        payload = {}
        # Getting response of URL
        #response = requests.request("POST", url, headers = headers)

        #if we want to use Basic auth then below is the code
        #response = requests.request("POST", url, headers=headers, data= payload,auth=HTTPBasicAuth(username="username", password="password"))
        response = requests.patch(SPSTATUS_API_BASE_URL,data=payload,headers=AUTHORIZATION_HEADER)
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        FailureResponse = jsonpath.jsonpath(json_reponse,'status')
        #print("\nthe success details :\n", FailureResponse)
        failure = FailureResponse[0]
        #print("\nThe json path/success code is: \n", failure)

        self.assertEqual(failure, "Failure - Resource not found")


    def test_dispense_api_with_patch_method(self):

        payload = {}
        # Getting response of URL
        #response = requests.request("POST", url, headers = headers)

        #if we want to use Basic auth then below is the code
        #response = requests.request("POST", url, headers=headers, data= payload, auth=HTTPBasicAuth(username="username", password="password"))
        response = requests.patch(DISPENSE_API_BASE_URL, data=payload, headers=AUTHORIZATION_HEADER)
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        FailureResponse = jsonpath.jsonpath(json_reponse,'status')
        #print("\nthe success details :\n", FailureResponse)
        failure = FailureResponse[0]
        #print("\nThe json path/success code is: \n", failure)

        self.assertEqual(failure, "Failure - Resource not found")



    def test_spStatus_api_with_delete_method(self):

        payload = {}
        # Getting response of URL
        #response = requests.request("POST", url, headers = headers)

        #if we want to use Basic auth then below is the code
        #response = requests.request("POST", url, headers=headers, data= payload,auth=HTTPBasicAuth(username="username", password="password"))
        response = requests.delete(SPSTATUS_API_BASE_URL,data=payload,headers=AUTHORIZATION_HEADER)
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        FailureResponse = jsonpath.jsonpath(json_reponse,'status')
        #print("\nthe success details :\n", FailureResponse)
        failure = FailureResponse[0]
        #print("\nThe json path/success code is: \n", failure)

        self.assertEqual(failure, "Failure - Resource not found")


    def test_dispense_api_with_delete_method(self):

        payload = {}
        # Getting response of URL
        #response = requests.request("POST", url, headers = headers)

        #if we want to use Basic auth then below is the code
        #response = requests.request("POST", url, headers=headers, data= payload, auth=HTTPBasicAuth(username="username", password="password"))
        response = requests.delete(DISPENSE_API_BASE_URL, data=payload, headers=AUTHORIZATION_HEADER)
        #print("The response is: \n", response)

        # Asserting to test the status code
        assert response.status_code == 404

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        #print("\nThe json response is: \n", json_reponse)

        # Fetch Json path
        FailureResponse = jsonpath.jsonpath(json_reponse,'status')
        #print("\nthe success details :\n", FailureResponse)
        failure = FailureResponse[0]
        #print("\nThe json path/success code is: \n", failure)

        self.assertEqual(failure, "Failure - Resource not found")


if __name__ == '__main__':
    unittest.main()


