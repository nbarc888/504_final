from flask import Flask, render_template
from google.cloud import storage
from datetime import timedelta

app = Flask(__name__)

def generate_signed_url(bucket_name, blob_name, expiration_minutes=15):
    """GCS Object Signed URL Generator"""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    url = blob.generate_signed_url(
        version="v4",
        expiration=timedelta(minutes=expiration_minutes),
        method="GET"
    )
    return url

@app.route('/')
def show_image():
    image_url = generate_signed_url(
        'instance-dog-279783831978',
        'ct-scan-of-ischemic-stroke.jpg'
    )
    return render_template('index.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)