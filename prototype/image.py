from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Replace with your actual public image URL
    image_url = "https://storage.cloud.google.com/instance-dog-279783831978/ct-scan-of-ischemic-stroke.jpg"
    return render_template('index.html', user_image_url=image_url)

