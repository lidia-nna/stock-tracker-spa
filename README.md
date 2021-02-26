# Stock Tracker

A VueJs/Flask SPA app to track selected stocks.

## Installation

1. Navigate to stock-tracker-spa api
```bash
cd stock-tracker-spa
```
2. Create and activate vertual env
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Set env variables, edit and run prereq.sh 
```bash
./prereq.sh
```
4. Install required python packages
```bash
pip install -r requirements.txt
````
5. Run API
```bash
flask run 
```
6. Navigate to web app component
```bash
cd stock-tracker-spa/stock-tracker-web
```
7. Ensure npm is downloaded and up to date (https://nodejs.org/en/download/)
```bash
npm install
npm run serve
```
8. Visit `http://localhost:8080` to check the app