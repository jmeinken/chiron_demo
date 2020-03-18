# chiron_demo

## Installation

- clone this repository
```
git clone [repository url]
```
- clone the chiron repository inside this repository
```
cd chiron_demo
git clone https://github.com/cchmc-bmi-os/chiron.git
```
- set up your python environment
```
# if desired, create and activate a virtual environment

# note: This demo uses a SQLite database. Django versions after 2.2 use a 
# SQLite version that is incompatible with older RedHat systems. If this
# applies to you, run pip install 'Django<2.2' first.

cd chiron
pip install -r requirements.txt
```
