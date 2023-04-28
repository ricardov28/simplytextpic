from flask import Flask, send_file
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Define the connection string and container name for your Azure Blob Storage
connection_string = "DefaultEndpointsProtocol=https;AccountName=ricostgiot123;AccountKey=EPSmvTHdZpjeKfUQkxGKXLbkb4uvZRX0Gp2z0/A4ekRUXeR1FKuyKrA9di3ZT0sTy7tJgvyK12JG+AStenVmPw=="
container_name = "messages01"

# Define a function to get the URL of the latest image in the container
def get_latest_image_url():
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()
    latest_blob = max(blobs, key=lambda b: b.last_modified)
    latest_blob_url = container_client.get_blob_client(latest_blob.name).url
    return latest_blob_url

@app.route('/')
def index():
    latest_image_url = get_latest_image_url()
    return f'<html><body style="background-color:black;"><p style="color:white;">This is the latest picture</p><img src="{latest_image_url}"></body></html>'

if __name__ == '__main__':
    app.run()
