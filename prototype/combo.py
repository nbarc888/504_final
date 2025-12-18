from flask import Flask, render_template_string

app = Flask(__name__)

# GCP bucket image URL
IMAGE_URL = "https://storage.googleapis.com/instance-dog-279783831978/ct-scan-of-ischemic-stroke.jpg"

# Combined HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NYS Medical - Rural Hospital</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #3d4247;
            color: #EFF0EF;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: #28d73b;
            text-align: center;
            margin-bottom: 30px;
        }
        h2 {
            color: #28d73b;
            text-align: center;
            margin-top: 40px;
        }
        .patient-info {
            background-color: #4a4f54;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            margin-bottom: 30px;
        }
        .patient-info p {
            font-size: 1.1em;
            line-height: 1.6;
            margin: 10px 0;
        }
        .vitals {
            background-color: #4a4f54;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            margin: 20px 0;
        }
        .vitals h3 {
            color: #28d73b;
            margin-top: 0;
            text-align: center;
        }
        .vitals p {
            font-size: 1em;
            text-align: center;
        }
        .imaging-section {
            background-color: #4a4f54;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            margin-top: 30px;
            text-align: center;
        }
        .imaging-section img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.4);
            margin-top: 15px;
        }
        .image-info {
            margin-top: 15px;
            color: #bbb;
            font-size: 0.9em;
        }
        .footer {
            margin-top: 40px;
            text-align: center;
            font-size: 0.9em;
            color: #999;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Remote Instance Connected Successfully</h1>
        
        <div class="patient-info">
            <p><strong>Patient:</strong> John Doe, 68M - MRN 123456</p>
            <p><strong>Admitted:</strong> 12/15/2025</p>
            <p><strong>Chief Complaint:</strong> New Onset Altered Mental Status</p>
            <p>Patient was found down at home by family member. Unwitnessed fall, Unknown LOC and Unknown HS.</p>
        </div>
        
        <div class="vitals">
            <h3>Vitals</h3>
            <p>BP: 178/102 mmHg | HR: 102 bpm | RR: 18 bpm | Temp: 98.6°F | SpO2: 96%</p>
        </div>
        
        <h2>Health History</h2>
        <div class="patient-info">
            <p><em>History Provided by Family Member</em></p>
            <p><strong>Past Medical History:</strong> HTN, HLD, Previous DVT in LLE s/p thrombectomy 2014</p>
            <p><strong>Allergies:</strong> No known allergies</p>
            <p><strong>Medications:</strong> Atorvastatin 10mg daily, Metoprolol 12.5mg daily</p>
        </div>
        
        <h2>Imaging Studies</h2>
        <div class="imaging-section">
            <h3 style="color: #28d73b; margin-top: 0;">CT Scan - Ischemic Stroke</h3>
            <img src="{{ image_url }}" alt="CT Scan of Ischemic Stroke">
            <div class="image-info">
                <p>Image from GCP Storage Bucket</p>
            </div>
        </div>
        
        <div class="footer">
            <p>NYS Medical - Rural Hospital Remote Consultation System</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, image_url=IMAGE_URL)

if __name__ == '__main__':
    # Run on all interfaces (so it's accessible via public IP), port 5003
    #app.run(debug=True, host='0.0.0.0', port=5003)
    app.run(host='0.0.0.0', port=5003)