import requests
import time

# API endpoint URL to test (replace with your API URL)
api_url = "https://twitter.com"

# Number of requests to send
num_requests = 5

# Time interval between requests (in seconds)
request_interval = 1  # Adjust this based on the API's rate limit

# API key or authorization token (if required)
headers = {
    "Authorization": "Bearer YOUR_API_KEY_HERE",  # Replace with your API key/token
}


def send_request():
    try:
        #response = requests.get(api_url, headers=headers)

        response = requests.get(api_url)
        if response.status_code == 200:
            print("Request successful")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {str(e)}")


# Send a specified number of requests with a delay


for i in range(num_requests):
    send_request()
    time.sleep(request_interval)

