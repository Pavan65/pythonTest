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

# Configuration
CREATECOPAYENROLLMENT_API_BASE_URL = config[environment]['CREATECOPAYENROLLMENT_API_BASE_URL']
PUSHCONSENTS_API_BASE_URL = config[environment]['PUSHCONSENTS_API_BASE_URL']
UPATEPATIENT_API_BASE_URL = config[environment]['UPATEPATIENT_API_BASE_URL']
UPDATEPATIENTCONSENTS_API_BASE_URL = config[environment]['UPDATEPATIENTCONSENTS_API_BASE_URL']


AUTHORIZATION_HEADER = {
'Content-Type': 'application/json',
    'Authorization': 'Bearer OHm3JxlDYuhymz5ymUdKmEEp9Zgy'
}
AUTHORIZATION_HEADER1 = {
'Content-Type': 'application/json'
}


# Test Cases Class
class TakedaCopayEnrollmentTestCase(unittest.TestCase):
    def test_createCopayEnrollment_api(self):

        json_input = {
    "channel": "hub",
    "brand": "entyvio",
    "patient": {
        "firstName": "xxxx",
        "lastName": "xxxx",
        "gender": "Female",
        "birthDate": "1977-03-21",
        "addressLine1": "xxxx",
        "city": "Lincoln",
        "state": "NE",
        "postalCode": "12345",
        "homePhone": "9876543210",
        "mobilePhone": "3331114444",
        "partnerId": "X5MEN4"
    },
    "referringPhysician": {
        "partnerId": "1-FJJC-811",
        "firstName": "Mark",
        "middleName": "G.",
        "lastName": "Griffin",
        "addressLine1": "4545 R ST LINCOLN NE",
        "city": "LINCOLN",
        "state": "NE",
        "postalCode": "68503",
        "workPhone": "4024654545",
        "fax": "4024655861",
        "npi": "1164416251"
    },
    "referralPractice": {
        "partnerId": "1-GBNZ-4001",
        "name": "MARK, GRIFFIN",
        "addressLine1": "4545 R ST LINCOLN NE",
        "city": "LINCOLN",
        "state": "NE",
        "postalCode": "68503",
        "phone": "4024654545"
    },
    "consents": [
        {
            "type": "hippa-authorization",
            "signedDate": "10/25/2018 12:00:00 AM"
        }
    ],
    "surveys": [
        {
            "name": "Entyvio Patient Survey v1.0.0",
            "description": "Entyvio Copay Enrollment Survey",
            "responses": [
                {
                    "key": "commercial-insurance",
                    "value": "yes"
                },
                {
                    "key": "government-insurance",
                    "value": "yes"
                },
                {
                    "key": "third-party-reimbursement",
                    "value": "yes"
                },
                {
                    "key": "eob-acknowledgement",
                    "value": "yes"
                }
            ]
        }
    ],
    "additionalInformation": {
        "annotations": [
            {
                "key": "service-request-id",
                "value": "1-X5OWRW",
                "displayName": "Covance Service Request Identifier",
                "description": "Service request identifier from Covance to be associated with the patient's enrollment membership."
            },
            {
                "key": "group-number",
                "value": "EC16301001",
                "displayName": "GroupNumber",
                "description": "Use this value to invoke correct group endpoint."
            }
        ]
    }
}

        json_input = json.dumps(json_input)
        start_time = time.time()

        # Make a POST request with Json input body
        if environment == "COPAY_DEV":
            response = requests.post(CREATECOPAYENROLLMENT_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER1)
        elif environment == "COPAY_QA":
            response = requests.post(CREATECOPAYENROLLMENT_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)
        elif environment == "COPAY_PROD":
            response = requests.post(CREATECOPAYENROLLMENT_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)
        else:
            print("Create PAtient API error :\nEnvironment was not chosen properly")
        end_time = time.time()

        # Asserting to test the status code
        assert response.status_code == 200
        elapsed_time = end_time - start_time

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        print('output response of Create copay enrollment API:\n',json_reponse, '\n')

        print(f"CreateCopayEnrollment API is reachable. Response time: {elapsed_time:.2f} seconds")

    def test_updatePatient_api(self):

        json_input = {
                "uid": "02cec0d7-59a3-e911-b819-005056a941b9",
                "partnerId": "HELLO54",
                "organizationMasterId": "null",
                "salutation": "null",
                "firstName": "Dianas",
                "middleName": "null",
                "lastName": "Merthas",
                "gender": "female",
                "birthDate": "1993-03-03",
                "addressLine1": "1113 Park Avenue",
                "addressLine2": "CrossRoad",
                "city": "Cedar",
                "state": "NY",
                "postalCode": "07929",
                "countryCode": "null",
                "homePhone": "1011181119",
                "mobilePhone": "1011181119",
                "workPhone": "1011181119",
                "extension": "null",
                "fax": "1011041119",
                "email": "shobhna.kurre9@connectiverx.com",
                "preferredContactMethod": "null",
                "preferredContactTime": "null",
                "ssn4": "null",
                "careGiver": "null",
                "insurances": [{
                                "payerName": "Aetna9",
                                "groupNumber": "GRP1234219",
                                "memberId": "123456219",
                                "bin": "BIN119",
                                "pcn": "PCN229"
                }]
}
        json_input = json.dumps(json_input)
        start_time = time.time()

        # Make a POST request with Json input body
        if environment == "COPAY_DEV":
            response = requests.put(UPATEPATIENT_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER1)
        elif environment == "COPAY_QA":
            response = requests.put(UPATEPATIENT_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)
        elif environment == "COPAY_PROD":
            response = requests.put(UPATEPATIENT_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)
        else:
            print("Update PAtient API error :\nEnvironment was not chosen properly")

        end_time = time.time()

        # Asserting to test the status code
        assert response.status_code == 200
        elapsed_time = end_time - start_time

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        print('output response of Update patient API:\n',json_reponse,'\n')

        print(f"UpdatePatient API is reachable. Response time: {elapsed_time:.2f} seconds")

    def test_updatePatientConsents_api(self):

        json_input = {
  "channel": "hub",
  "brand": "entyvio",
  "consents": [
    { "type": "hippa-authorization", "signedDate": "2018-09-15" },
    { "type": "third-party-disclosure", "signedDate": "2018-09-15" },
    { "type": "phone-communication", "signedDate": "2018-09-15" }
   ]
}
        json_input = json.dumps(json_input)
        start_time = time.time()

        # Make a POST request with Json input body
        if environment == "COPAY_DEV":
            response = requests.put(UPDATEPATIENTCONSENTS_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER1)
        elif environment == "COPAY_QA":
            response = requests.put(UPDATEPATIENTCONSENTS_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)
        elif environment == "COPAY_PROD":
            response = requests.put(UPDATEPATIENTCONSENTS_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)
        else:
            print("Update PAtient Consents API error :\nEnvironment was not chosen properly")

        end_time = time.time()

        # Asserting to test the status code
        assert response.status_code == 200
        elapsed_time = end_time - start_time

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        print('output response of Update patient API:\n',json_reponse,'\n')

        print(f"UpdatePatientConsents API is reachable. Response time: {elapsed_time:.2f} seconds")



    def test_pushConsensts_Merkle_api(self):

        json_input =  {
     "message": {
       "attributes": {
         "key": "value"
       },
       "data": "ewogICJLQ1JNSUQiOiAiQSIsCiAgIlZlbmRvcmNvbnN1bWVySUQiOiAiMDI2YTJkZWU4ZDA2NGZhNmE2ZTljYTI2Mzk0MWYzODkiLAogICJBTk9OWU1PVVNfVVNFUl9JRCI6ICJjYzI2YWVmZC0wYzcxLTRhYjQtOWQwMS00ZGVkZTE3Yjg4YmYiLAogICJQYXRpZW50X0ZpcnN0bmFtZSI6ICJLaXJhIiwKICAiUGF0aWVudF9MYXN0bmFtZSI6ICJCb2t1d2EiLAogICJQYXRpZW50X0VtYWlsIjogImV4YW1wbGVfZW1haWxAZ21haWwuY29tIiwKICAiUGF0aWVudF9BZGRyZXNzMSI6ICIxMDAgbWFpbiBzdCIsCiAgIlBhdGllbnRfQWRkcmVzczIiOiAiQSIsCiAgIlBhdGllbnRfWmlwIjogIjk4NjY2IiwKICAiUGF0aWVudF9DaXR5IjogIlNISU5BR0FNSUNJVFkiLAogICJQYXRpZW50X1N0YXRlIjogIklMIiwKICAiUGF0aWVudF9QaG9uZSI6ICIoMTExKSAyMjItMzMzMyIsCiAgIlBhdGllbnRfRE9CIjogIjIwMjMxMDEyIiwKICAiUGF0aWVudF9HZW5kZXIiOiAiTSIsCiAgIlByZXNjcmliZXJfRmlyc3RuYW1lIjogIkEiLAogICJQcmVzY3JpYmVyX0xhc3RuYW1lIjogIkEiLAogICJQcmVzY3JpYmVyX0FkZHJlc3MxIjogIkEiLAogICJQcmVzY3JpYmVyX0FkZHJlc3MyIjogIkEiLAogICJQcmVzY3JpYmVyX1ppcCI6ICJBIiwKICAiUHJlc2NyaWJlcl9DaXR5IjogIkEiLAogICJQcmVzY3JpYmVyX1N0YXRlIjogIkEiLAogICJQcmVzY3JpYmVyX1Bob25lTnVtYmVyIjogIkEiLAogICJQYXRpZW50X1VDIjogIk4iLAogICJQYXRpZW50X0NEIjogIlkiLAogICJPbl9FbnR5dmlvIjogIkEiLAogICJGaXJzdEluZnVzaW9uTW9udGgiOiAiOSIsCiAgIkZpcnN0SW5mdXNpb25ZZWFyIjogIjIwMTkiLAogICJQcmV2aW91c2x5VGFraW5nT3RoZXJCaW9sb2dpY3MiOiAiUmVtaWNhZGUiLAogICJDdXJyZW50bHlUYWtpbmdPdGhlckJpb2xvZ2ljcyI6ICJSZW1pY2FkZSIsCiAgIkRpZ2l0YWxTaWduYXR1cmUiOiAiQSIsCiAgIkNvcGF5X0NvbnNlbnQiOiAiWSIsCiAgIkNvbnNlbnRfUmVjZWl2ZWQiOiAiQSIsCiAgIkNvcGF5YXRUZXN0MSI6ICJBIiwKICAiQ29wYXlhdFRlc3QyIjogIkEiLAogICJDb3BheWF0VGVzdDMiOiAiQSIsCiAgIkNvcGF5YXRUZXN0NCI6ICJBIiwKICAiUmVnaXN0cmF0aW9uU291cmNlIjogIldFQiIsCiAgIldlYlJlZ2lzdHJhdGlvblNvdXJjZVVSTCI6ICJodHRwczovL3d3dy5lbnR5dmlvLmNvbS9ib29rIiwKICAiUmVnaXN0cmF0aW9uRGF0ZSI6ICJBIiwKICAiU2VsZWN0U2VydmljZXNfTlMiOiAiQSIsCiAgIlNlbGVjdFNlcnZpY2VzX0ZTIjogIkEiLAogICJMZWFkX1NvdXJjZSI6ICJXZWIiLAogICJXZWJfdXRtX2NhbXBhaWduIjogIkJyYW5kLUVudHl2aW8tRVgiLAogICJXZWJfdXRtX21lZGl1bSI6ICJjcGMiLAogICJXZWJfdXRtX2NvbnRlbnQiOiAiRW50eXZpbyIsCiAgIldlYl91dG1fdGVybSI6ICJlbnR5dmlvIiwKICAiV2ViX3V0bV9zb3VyY2UiOiAiYmluZyIsCiAgIkNvcGF5Q2FyZElEIjogIkEiLAogICJDb3BheVN0YXR1cyI6ICJBIgp9",
       "messageId": "1111111118"
     },
     "subscription": "projects/myproject/subscriptions/mysubscription"
   }

        json_input = json.dumps(json_input)
        start_time = time.time()

        # Make a POST request with Json input body
        if environment == "COPAY_DEV":
            response = requests.post(PUSHCONSENTS_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER1)
        elif environment == "COPAY_QA":
            response = requests.post(PUSHCONSENTS_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER1)
        elif environment == "COPAY_PROD":
            response = requests.post(PUSHCONSENTS_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER1)
        else:
            print("Push Consents API error :\nEnvironment was not chosen properly")

        end_time = time.time()

        # Asserting to test the status code
        assert response.status_code == 201
        elapsed_time = end_time - start_time

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)
        print('output response of push consents API:\n',json_reponse, '\n')

        # Fetch Json path
        message = jsonpath.jsonpath(json_reponse, 'status')[0]

        # Asserting to test the error description
        self.assertEqual(message, "Record inserted successfully.")
        print(f"PushConsents API is reachable. Response time: {elapsed_time:.2f} seconds")


if __name__ == '__main__':
    unittest.main()



