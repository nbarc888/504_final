from flask import Flask, render_template_string

app = Flask(__name__)

# GCP bucket image URL
IMAGE_URL = "https://storage.googleapis.com/instance-dog-279783831978/ct-scan-of-ischemic-stroke.jpg"

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GCP Image Display</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            max-width: 1000px;
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        .image-info {
            margin-top: 15px;
            color: #666;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>CT Scan - Ischemic Stroke</h1>
        <img src="{{ image_url }}" alt="CT Scan of Ischemic Stroke">
        <div class="image-info">
            <p>Image from GCP Storage Bucket</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, image_url=IMAGE_URL)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)