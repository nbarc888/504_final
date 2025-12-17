from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_image():
    # Use the public URL directly
    image_url = "https://storage.googleapis.com/instance-dog-279783831978/ct-scan-of-ischemic-stroke.jpg"
    return render_template('index.html', image_url=image_url)

#### Run line of code within google cloud CLI 
### gsutil iam ch allUsers:objectViewer gs://instance-dog-279783831978/ct-scan-of-ischemic-stroke.jpg