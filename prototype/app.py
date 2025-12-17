from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route("/")
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
        


if __name__ == "__main__":
    # Run on all interfaces (so it's accessible via public IP), port 5003
    app.run(host="0.0.0.0", port=5003)