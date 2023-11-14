import json
import requests
import subprocess


def send_request(url: str, message: str="") -> None:
    token = '{}'.format(subprocess.Popen(
        args="gcloud auth print-identity-token",
        stdout=subprocess.PIPE,
        shell=True).communicate()[0]
        )[2:-3]
    
    if message == "":
        # Send an HTTP GET request to the URL
        response = requests.get(url)
    else:
        # Convert the message to a JSON string
        json_data = json.dumps(message)
        
        headers = {
            "Authorization": "Bearer {}".format(token),
            "Content-Type": "application/json",
        }

        # Send an HTTP POST request with the JSON data
        response = requests.post(url, data=json_data, headers=headers)
        
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Request was successful.")
        print("Response content: ", response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    json_file = "data.json"

    with open(json_file, "r") as file:
        data = json.load(file)
        
    url = "CLOUD_FUNCTION/URL"
    
    send_request(url=url, message=data)
    