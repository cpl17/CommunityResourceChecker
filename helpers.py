import requests 
import json
import time

def make_request(search_string,prefix):

    time.sleep(1.5)

    url = "https://api.bing.microsoft.com/v7.0/custom/search"
    headers = {
        "Ocp-Apim-Subscription-Key": "e8a37dae9cbe4759bcb3689bb35c24ea"
    }

    # Define the query parameters
    params = {
        "q": f'"{search_string}" + {prefix}',
        "customconfig": "53068398-472d-48e0-b1d4-95ac66b7eaf9",
        "mkt": "en-US",
        "answerCount":1
    }

    # Make the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:

        # # Save the response to a JSON file
        # with open("response_temp.json", "w") as json_file:
        #     json.dump(response.json(), json_file)
        
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        return None