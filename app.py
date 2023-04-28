from flask import Flask, send_file
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Define the connection string and container name for your Azure Blob Storage
connection_string = "your_connection_string"
container_name = "your_container_name"

# Define a function to get the URL of the latest image in the container
def get_latest_image_url():
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    blobs = container_client.list_blobs()
    latest_blob = max(blobs, key=lambda b: b.last_modified)
    latest_blob_url = container_client.get_blob_client(latest_blob.name).url
    return latest_blob_url


# a JavaScript function updateImage() that updates the src attribute of the <img> tag every one second. 
# The setInterval() function calls the updateImage() function every one second, and the new Date().getTime()
# expression appends a unique timestamp to the URL to ensure that the browser does not cache the image.
@app.route('/')
def index():
    latest_image_url = get_latest_image_url()
    return f'<html><body style="background-color:black;"><p style="color:white;">This is the latest picture</p><img id="latest-image" src="{latest_image_url}"></body><script>setInterval(updateImage, 1000);function updateImage(){{var image = document.getElementById("latest-image");image.src = "{latest_image_url}" + "?" + new Date().getTime();}}</script></html>'

if __name__ == '__main__':
    app.run()
