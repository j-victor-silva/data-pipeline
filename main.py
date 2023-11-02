import requests
import json


key_path = "local-sprite-402222-12c4e0fe07a9.json"

with open(key_path, "r") as key_file:
    key_data = json.load(key_file)

def send_request(url: str, message: str="") -> None:
    if message == "":
        # Send an HTTP GET request to the URL
        response = requests.get(url)
    else:
        # Convert the message to a JSON string
        json_data = json.dumps(message)
        
        headers = {
            "Content-Type": "application/json",
        }

        # Send an HTTP POST request with the JSON data
        response = requests.post(url, data=json_data, headers=headers)
        
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Request was successful.")

        print("Response content:")
        print(response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    json_file = "data.json"

    with open(json_file, "r") as file:
        data = json.load(file)
        
    url = "https://us-central1-local-sprite-402222.cloudfunctions.net/send_message_to_pubsub"
    
    send_request(url=url, message=data)
    