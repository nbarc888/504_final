At this Current time(12/17/25 2pm EST): Code is non-functional due to issues with deploying flask app 
Primary methodology is to use flask app to display an image from a GCP bucket which can bee seen in '504_final_opt.ipynb' which is a notebook that can connect to both the VM and the google bucket. 


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

### Due to Price variability between both Azure and GCP, GCP was selected to run prototype. 


For GCP VM instance
Machine and size: E2-small 
US-east4 - Northern Virginia
### connect access to all cloud APIs

For GCP VM Bucket
name: instance-dog-279783831978

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
### Bucket-Connect options
```bash
### to connect to bucket 
sudo apt install git
```
```bash
export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
```
```bash
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```
```bash
sudo apt-get update
sudo apt-get install gcsfuse
```
```bash
gcsfuse -v
```

####

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
cd prototype/
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python app.py
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