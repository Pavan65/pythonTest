import time

import requests

# API endpoint URL to test (replace with your API URL)
api_url = "https://twitter.com"


def test_api_ping(api_url):
    try:
        start_time = time.time()
        response = requests.get(api_url)
        end_time = time.time()

        if response.status_code == 200:
            elapsed_time = end_time - start_time
            print(f"API is reachable. Response time: {elapsed_time:.2f} seconds")
        else:
            print(f"API is not reachable. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Call the function to test the API


test_api_ping(api_url)