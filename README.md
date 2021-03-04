# Stock Tracker

A VueJs/Flask SPA app to track selected stocks.

## Live demo

[https://lidia-nna.github.io/stock-tracker-spa]

## Installation for local use

1. Clone the repo and navigate to stock-tracker-spa directory
```bash
git clone https://github.com/lidia-nna/stock-tracker-spa.git
cd stock-tracker-spa
```
2. Create and activate vertual env
```bash
python3 -m venv your-venv
source your-venv/bin/activate
```
3. Set env variables: edit  `.env` file 
```bash
nano .env
export $(cat .env)
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