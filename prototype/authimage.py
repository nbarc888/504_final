from flask import Flask, render_template_string, send_file
import requests
import os

app = Flask(__name__)

# GCP bucket image URL
IMAGE_URL = "https://storage.cloud.google.com/instance-dog-279783831978/ct-scan-of-ischemic-stroke.jpg"
LOCAL_IMAGE_PATH = "ct-scan.jpg"

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CT Scan Viewer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
        .container {
            background-color: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            max-width: 1000px;
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 28px;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 16px;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            border: 3px solid #667eea;
        }
        .image-info {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 8px;
            color: #555;
            font-size: 14px;
        }
        .status {
            display: inline-block;
            padding: 5px 15px;
            background-color: #28a745;
            color: white;
            border-radius: 20px;
            font-size: 12px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏥 Medical Imaging Viewer</h1>
        <p class="subtitle">CT Scan - Ischemic Stroke</p>
        <img src="/image" alt="CT Scan of Ischemic Stroke">
        <div class="image-info">
            <p><strong>Source:</strong> GCP Storage Bucket</p>
            <p><strong>Bucket:</strong> instance-dog-279783831978</p>
            <div class="status">✓ Image Loaded Successfully</div>
        </div>
    </div>
</body>
</html>
"""

def download_image():
    """Download image from GCP bucket if not already cached"""
    if not os.path.exists(LOCAL_IMAGE_PATH):
        print(f"Downloading image from {IMAGE_URL}...")
        try:
            response = requests.get(IMAGE_URL, timeout=10)
            response.raise_for_status()
            with open(LOCAL_IMAGE_PATH, 'wb') as f:
                f.write(response.content)
            print("Image downloaded successfully!")
        except Exception as e:
            print(f"Error downloading image: {e}")
            return False
    return True

@app.route('/')
def index():
    download_image()
    return render_template_string(HTML_TEMPLATE)

@app.route('/image')
def serve_image():
    """Serve the image file"""
    if os.path.exists(LOCAL_IMAGE_PATH):
        return send_file(LOCAL_IMAGE_PATH, mimetype='image/jpeg')
    else:
        # Fallback to direct URL if local file doesn't exist
        try:
            response = requests.get(IMAGE_URL, timeout=10)
            response.raise_for_status()
            return send_file(BytesIO(response.content), mimetype='image/jpeg')
        except Exception as e:
            return f"Error loading image: {e}", 500

if __name__ == '__main__':
    # Download image on startup
    download_image()
    print("Starting Flask app on http://0.0.0.0:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)