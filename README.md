# Data Pipeline with Python
This project consists of a pipeline that sends a JSON file with data that will be inserted into a table in BigQuery using Python to send an HTTP request from a trigger in a GitHub Action, then a Cloud Function in GCP receives the data sent via the POST request and sends it to a Pub/Sub topic, a subscription reads this message and writes it to the BigQuery table.

## Technologies

- Python and packages:
	- requests
	- json
	- subprocess
	- google-cloud
- GCloud
- GitHub Actions
- Cloud Function
- Pub/Sub
- BigQuery

## Prerequisites

- A GCP account with permissions to create a Cloud Function, a topic and a subscription in Pub/Sub (optional to have permissions to create a dataset and table in BigQuery if they do not exist)
- GCP or SA account credentials JSON file
- An SA authenticated in [_gcloud_](https://cloud.google.com/docs/authentication/gcloud?hl=pt-br) with permissions to send requests to the Cloud Function (can be replaced with your own account if it has the permissions)

## Installation

First, we will clone the project, then create your own repository on **GitHub** to store your project and create your GitHub Action.
Then, create a **Cloud Function** with the Python language and copy the code into the "*cloud_function.py*" file, deploy it and add permission for yourself or the SA to have the role of "**Cloud Function Administrator**".
Change line **43** of the "*main.py*" file to the URL of your Cloud Function, and lines **11** and **13** to your project id and the name of your Pub/Sub topic respectively.

> *It's important to remember to put your account or SA credentials file in .gitignore to avoid uploading it to your repository!*

Create your topic in Pub/Sub and the subscription linked to it, in your subscription settings select the option to write to BigQuery and select the destination table (create it if it does not exist).
With all these steps done, let's save our credentials file in a repository secret on GitHub with the name "***GCP_CREDENTIALS***".

## Running

To run the project, first follow the **schema pattern** of your table in BigQuery to create the fictitious data in the "*data.json*" file, for example, in my table the schema has only two columns named: **name** of type **String** and **age** of type **INT64**. In the "*data.json*" file, for example, it only has these two columns.
To make the GitHub Action run you need to change this file whenever you want to insert new data.
Push the changes and check your Action to see if everything is working. After it finishes executing, check the table in BigQuery with the new data.
