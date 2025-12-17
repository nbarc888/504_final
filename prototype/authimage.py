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

def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>NYS Medical - Rural Hospital</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #3d4247;
            color: #EFF0EF;
            text-align: center;
            margin: 50px;
          }
          h1 {
            color: #28d73b;
          }
          p {
            font-size: 1.2em;
          }
          .footer {
            margin-top: 40px;
            font-size: 0.9em;
            color: #777;
          }
        </style>
      </head>
      <body>
        <h1> Remote Instance Connected Successfully.  </h1>
        <p>
          John Doe 68M - MRN 123456<br>
          Admitted: 12/15/2025<br>
            Chief Complaint: New Onset Altered Mental Status <br>
            Patient was found down at home by family member. Unwitnessed fall, Unknown LOC and Unknown HS. <br>
        </p>
        <div class="footer">
          <p> Vitals </p>
            <p> BP: 178/102 mmHg | HR: 102 bpm | RR: 18 bpm | Temp: 98.6°F | SpO2: 96% </p>
        </div>
        <h2> Health History </h2>
        
          <p> History Provided by Family Member </p>
          <p> HTN, HLD, Previous DVT in LLE s/p thrombectomy 2014 </p>
          <p> No known allergies </p>
          <p> Medications: Atorvastatin 10mg daily, Metoprolol 12.5mg daily </p>
      
      </body>
    </html>
    """
     


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003)