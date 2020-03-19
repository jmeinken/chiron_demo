# chiron_demo

## Installation

- clone this repository
```
git clone https://github.com/jmeinken/chiron_demo.git
```
- clone the chiron repository inside this repository
```
cd chiron_demo
git clone https://github.com/cchmc-bmi-os/chiron.git
```
- set up your python environment
```
# if desired, create and activate a virtual environment

# note: This demo uses a prebuilt SQLite database. Django versions after 2.2 use a 
# SQLite version that is incompatible with older RedHat systems. If this
# applies to you, run pip install 'Django<2.2' first.

cd chiron
pip install -r requirements.txt
```
- edit chiron_demo/settings.py to point to your mongo installation
```
# no mongo authentication
CHIRON_MONGO_DATABASE_NAME = 'chiron_demo'
CHIRON_MONGO_CONNECTION_SETTINGS = {
  'host' : 'localhost',
}

# with mongo authentication
CHIRON_MONGO_DATABASE_NAME = 'chiron_demo'
CHIRON_MONGO_CONNECTION_SETTINGS = {
  'host' : 'localhost',
  'username' : 'myusername',
  'password' : '...',
  'authSource' : 'admin',
}
```
- populate your mongo database with the dummy data from the patient_data models
```
python manage.py chiron_run_etl
```
- run the dev server and go to http://localhost:8000
- enter username and password as "admin" and "admin"

