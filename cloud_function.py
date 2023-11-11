import os
from google.cloud import pubsub_v1

def publish_to_pubsub(request):
    request_json = request.get_json()
    
    if not request_json:
        return 'No data provided in request', 400

    # Replace 'your-project-id' with your Google Cloud project ID
    project_id = 'local-sprite-402222'
    # Replace 'your-topic-name' with the name of your Pub/Sub topic
    topic_name = 'send-message-to-bigquery'

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    future = publisher.publish(topic_path, request_json.encode('utf-8'))

    return f"Message published to Pub/Sub topic: {topic_path}", 200
