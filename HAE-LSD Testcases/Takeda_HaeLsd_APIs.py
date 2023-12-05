import json
import unittest
import jsonpath
import time
import requests
import configparser

# Exception Class
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Load configuration from the file
config = configparser.ConfigParser()
config.read('config.ini')

# Choose the environment here (DEV or PROD)
environment = "HAELSD_QA"

# Configuration
PATIENTS_API_BASE_URL = config[environment]['PATIENTS_API_BASE_URL']
PRESCRIBERS_API_BASE_URL = config[environment]['PRESCRIBERS_API_BASE_URL']
SITEOFCARE_API_BASE_URL = config[environment]['SITEOFCARE_API_BASE_URL']
SPECIALITYPHARMACIRES_API_BASE_URL = config[environment]['SPECIALITYPHARMACIRES_API_BASE_URL']
PAYERS_API_BASE_URL = config[environment]['PAYERS_API_BASE_URL']
SPSTATUS_API_BASE_URL = config[environment]['SPSTATUS_API_BASE_URL']
DISPENSE_API_BASE_URL = config[environment]['DISPENSE_API_BASE_URL']

AUTHORIZATION_HEADER = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 4Ymt8br8rs4JAPIZJZKxYzpff9Zn'
        }


# Test Cases Class
class TakedaHaeLsdEnrollmentTestCase(unittest.TestCase):


    def test_patients_api(self):
        json_input = {
    "context": {
        "sourceSystem": "Takeda Intient",
        "targetSystem": "Vendor Name1",
        "dataScenario": "Export of Takeda Id",
        "dateSent": "2017-11-01T00:00:00",
        "transactionId": "e93q9-323r3r-3rqwew-34d1"
    },
    "body": {
        "patients": [
            {
                "patientTakedaId": "PA262001",
                "patientConsentedFlag": "N",
                "brandName": "Takhzyro"
            },
            {
                "patientTakedaId": "PA262002",
                "patientConsentedFlag": " Y",
                "brandName": "Firazyr"
            },
            {
                "patientTakedaId": "PA262003",
                "patientConsentedFlag": "Y",
                "brandName": "Cinryze"
            },
            {
                "patientTakedaId": "PA262004",
                "patientConsentedFlag": "N",
                "brandName": "Takhzyro"
            }
        ]
    }
}
        json_input = json.dumps(json_input)

        # Make a POST request with Json input body
        response = requests.post(PATIENTS_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successtext = jsonpath.jsonpath(json_reponse, 'body')

        success = successtext[0]['successDetail']['message']

        # Asserting to test the success description
        self.assertEqual(success, "Patients Request received successfully.")

    def test_prescribers_api(self):
        json_input = {
    "context": {
        "sourceSystem": "Takeda Intient",
        "targetSystem": "Vendor Name1",
        "dataScenario": "Export of Takeda Id",
        "dateSent": "2017-11-02T00:00:00",
        "transactionId": "e93q9-323r3r-3rqwew-34d3"
    },
    "body": {
        "prescribers": [
            {
                "prescriberTakedaId": "PH735001",
                "prescriberNameFirst": "Daniel",
                "prescriberNameLast": "Griffin",
                "prescriberNPI": "1093796724"
            },
            {
                "prescriberTakedaId": "PH735002",
                "prescriberNameFirst": "Sapna",
                "prescriberNameLast": "Reddy",
                "prescriberNPI": "1023015708"
            },
            {
                "prescriberTakedaId": "PH735003",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "trump",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873572"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "mcdonald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873573"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "red",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873574"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "orange",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873575"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "test1",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873576"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "test2",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873577"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "test3",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873578"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            },
            {
                "prescriberTakedaId": "PH735004",
                "prescriberNameFirst": "Ronald",
                "prescriberNameLast": "Green",
                "prescriberNPI": "1003873571"
            }
        ]
    }
}
        json_input = json.dumps(json_input)

        # Make a POST request with Json input body
        response = requests.post(PRESCRIBERS_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successtext = jsonpath.jsonpath(json_reponse, 'body')

        success = successtext[0]['successDetail']['message']

        # Asserting to test the success description
        self.assertEqual(success, "Prescribers Request received successfully.")


    def test_siteOfCare_api(self):
        json_input = {
    "context": {
        "sourceSystem": "Takeda Intient",
        "targetSystem": "Vendor Name1",
        "dataScenario": "Export of Takeda Id",
        "dateSent": "2017-11-01T00:00:00",
        "transactionId": "e93q9-323r3r-3rqwew-34d4"
    },
    "body": {
        "sitesOfCare": [
            {
                "socTakedaID": "PO897601",
                "socName": "Southern Or Internal Medicine",
                "socAddressLine1": "2900 Doctors Park Dr",
                "socAddressLine2": "Ste 200",
                "socAddressLine3": "socAddressLine3",
                "socAddressLine4": "socAddressLine4",
                "socCity": "Suite 10525",
                "socState": "Hopkins",
                "socZip": "500055",
                "socZip4": "500045",
                "socPostalCode": "post123",
                "socCountry": "Red Circle Driv"
            },
            {
                "socTakedaID": "PO897602",
                "socAddressLine1": "2900 Doctors Park Dr",
                "socAddressLine2": "10900 Red Circle Drive",
                "socAddressLine3": "Hopkins|",
                "socAddressLine4": "Suite 25",
                "socCity": "Suite 10525",
                "socState": "Hopkins",
                "socZip": "500055",
                "socZip4": "500045",
                "socPostalCode": "post123",
                "socCountry": "Red Circle Driv"
            },
            {
                "socTakedaID": "PO897603",
                "socName": "Southern Or Internal Medicine",
                "socAddressLine1": "Pharm.D.",
                "socAddressLine2": "10900 Red Circle Drive",
                "socAddressLine3": "Hopkins|",
                "socAddressLine4": "Suite 25",
                "socCity": "Suite 10525",
                "socState": "Hopkins",
                "socZip": "500055",
                "socZip4": "500045",
                "socPostalCode": "post123",
                "socCountry": "Red Circle Driv"
            },
            {
                "socTakedaID": "PO897604",
                "socName": "Southern Or Internal Medicine",
                "socCity": "Suite 10525",
                "socState": "Hopkins",
                "socZip": "500055",
                "socZip4": "500045",
                "socPostalCode": "post123",
                "socCountry": "Red Circle Driv"
            },
            {
                "socTakedaID": "PO897605",
                "socAddressLine2": "10900 Red Circle Drive",
                "socAddressLine3": "Hopkins|",
                "socAddressLine4": "Suite 25",
                "socCity": "Suite 10525",
                "socState": "Hopkins",
                "socZip": "500055",
                "socZip4": "500045",
                "socPostalCode": "post123",
                "socCountry": "Red Circle Driv"
            }
        ]
    }
}
        json_input = json.dumps(json_input)

        # Make a POST request with Json input body
        response = requests.post(SITEOFCARE_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successtext = jsonpath.jsonpath(json_reponse, 'body')

        success = successtext[0]['successDetail']['message']

        # Asserting to test the success description
        self.assertEqual(success, "SitesOfCare Request received successfully.")


    def test_specialityPharmacies_api(self):
        json_input = {
    "context": {
        "sourceSystem": "Takeda Intient",
        "targetSystem": "Vendor Name1",
        "dataScenario": "Export of Takeda Id",
        "dateSent": "2017-11-01T00:00:00",
        "transactionId": "e93q9-323r3r-3rqwew-33r3"
    },
    "body": {
        "spPharmacies": [
            {
                "spTakedaId": "SP001",
                "spName": "Pharmacare"
            },
            {
                "spTakedaId": "SP002",
                "spName": "IngenioRX"
            },
            {
                "spTakedaId": "SP003",
                "spName": "White Drug"
            },
            {
                "spTakedaId": "SP004",
                "spName": "Sentara"
            },
            {
                "spTakedaId": "SP005",
                "spName": "Pharmacare"
            }
        ]
    }
}
        json_input = json.dumps(json_input)

        # Make a POST request with Json input body
        response = requests.post(SPECIALITYPHARMACIRES_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successtext = jsonpath.jsonpath(json_reponse, 'body')

        success = successtext[0]['successDetail']['message']

        # Asserting to test the success description
        self.assertEqual(success, "Sp-Pharmacies Request received successfully.")


    def test_payers_api(self):
        json_input = {
    "context": {
        "sourceSystem": "Takeda Intient",
        "targetSystem": "Vendor Name1",
        "dataScenario": "Export of Takeda Id",
        "dateSent": "2017-11-01T00:00:00",
        "transactionId": "e93q9-323r3r-3rqwew-11-0000"
    },
    "body": {
        "payers": [
            {
                "payerPrimaryTakedaId": "PUUU897601",
                "payerName": "Unassigned Payer - Tschida",
                "payerCity": "Suite 10525",
                "payerState": "Hopkins",
                "payerZip": "500055",
                "payerZip4": "500045",
                "payerPostalCode": "post123",
                "payerCountry": "Red Circle Driv"
            },
            {
                "payerPrimaryTakedaId": "PUUU897602",
                "payerAddressLine2": "10900 Red Circle Drive",
                "payerAddressLine3": "Hopkins|",
                "payerAddressLine4": "Suite 25",
                "payerCity": "Suite 10525",
                "payerState": "Hopkins",
                "payerZip": "500055",
                "payerZip4": "500045",
                "payerPostalCode": "post123",
                "payerCountry": "Red Circle Driv"
            },
            {
                "payerPrimaryTakedaId": "PUUU897603",
                "payerName": "Unassigned Payer - Tschida",
                "payerAddressLine1": "Pharm.D.",
                "payerAddressLine2": "10900 Red Circle Drive",
                "payerAddressLine3": "Hopkins|",
                "payerAddressLine4": "Suite 25",
                "payerCity": "Suite 10525",
                "payerState": "Hopkins",
                "payerZip": "500055",
                "payerZip4": "500045",
                "payerPostalCode": "post123",
                "payerCountry": "Red Circle Driv"
            },
            {
                "payerPrimaryTakedaId": "PUUU897604",
                "payerName": "Unassigned Payer - Tschida",
                "payerCity": "Suite 10525",
                "payerState": "Hopkins",
                "payerZip": "500055",
                "payerZip4": "500045",
                "payerPostalCode": "post123",
                "payerCountry": "Red Circle Driv"
            },
            {
                "payerPrimaryTakedaId": "PUUU897605",
                "payerAddressLine2": "10900 Red Circle Drive",
                "payerAddressLine3": "Hopkins|",
                "payerAddressLine4": "Suite 25",
                "payerCity": "Suite 10525",
                "payerState": "Hopkins",
                "payerZip": "500055",
                "payerZip4": "500045",
                "payerPostalCode": "post123",
                "payerCountry": "Red Circle Driv"
            },
            {
                "payerPrimaryTakedaId": "PUUU897606",
                "payerName": "Unassigned Payer - Tschida",
                "payerAddressLine1": "Pharm.D.",
                "payerAddressLine2": "10900 Red Circle Drive",
                "payerAddressLine3": "Hopkins|",
                "payerAddressLine4": "Suite 25",
                "payerCity": "Suite 10525",
                "payerState": "Hopkins",
                "payerZip": "500055",
                "payerZip4": "500045",
                "payerPostalCode": "post123",
                "payerCountry": "Red Circle Driv"
            },
            {
                "payerPrimaryTakedaId": "PUUU897607",
                "payerName": "Unassigned Payer - Tschida",
                "payerCity": "Suite 10525",
                "payerState": "Hopkins",
                "payerZip": "500055",
                "payerZip4": "500045",
                "payerPostalCode": "post123",
                "payerCountry": "Red Circle Driv"
            }
        ]
    }
}
        json_input = json.dumps(json_input)

        # Make a POST request with Json input body
        response = requests.post(PAYERS_API_BASE_URL, json_input, headers=AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successtext = jsonpath.jsonpath(json_reponse, 'body')

        success = successtext[0]['successDetail']['message']

        # Asserting to test the success description
        self.assertEqual(success, "Payers Request received successfully.")


    @unittest.skip("Outbound API SpStatus is skipping")
    def test_spStatus_api_with_AuthorizationToken(self):

        # Getting response of URL
        response = requests.request("GET", SPSTATUS_API_BASE_URL, headers = AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successDetails = jsonpath.jsonpath(json_reponse,'body')
        success = successDetails[0]['successDetail']['message']

        self.assertEqual(success, "Status data is being posted to Takeda")

    @unittest.skip("Outbound API Dispense is skipping")
    def test_dispense_api_with_AuthorizationToken(self):

        # Getting response of URL
        response = requests.request("GET", DISPENSE_API_BASE_URL, headers = AUTHORIZATION_HEADER)

        # Asserting to test the status code
        assert response.status_code == 200

        # Displaying the response in JSON Formate
        json_reponse = json.loads(response.text)

        # Fetch Json path
        successDetails = jsonpath.jsonpath(json_reponse,'body')
        success = successDetails[0]['successDetail']['message']

        self.assertEqual(success, "Dispense data is being posted to Takeda")


if __name__ == '__main__':
    unittest.main()

