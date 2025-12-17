Log into Azure 

Create Virtual Machine with Following items:
Region - US - East US
Availability Zone 3
Image : Ubuntu Server 24.04 LTS x64 Gen2 
VM architecture x64
Size: Standard_F1s- 1 vcpu, 2 GiB memory (36.28 USD/monthly)

Admin account
username: dog
password: German$hepherd

Allow Selected port: SHH (22)

----------------
For GCP 
Machine and size: E2-small 
US-east4 - Northern Virginia


GCP DIrections : 
Insert following codes
```bash
sudo apt update 
```
```bash
sudo apt install python3 python3-pip python3-venv
```
```bash
sudo apt install git
```
```bash
git clone https://github.com/nbarc888/504_final.git
```
```bash
ls -l
```
```bash
cd 504_final/

```
```bash
ls -l
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r protoype/requirements.txt
```
```bash
python protoype/app.py
```


Azure directions

Quick Start for Github

```bash
git clone https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart
```

To run locally on device 
```bash
cd msdocs-python-flask-webapp-quickstart
```
```bash
py -m venv .venv
.venv\scripts\activate
```
```bash 
pip install -r requirements.txt
```
```bash
flask run prototype/app.py
```