# Credit Scoring Web App
## Overview
This credit scoring web app is based on the bank scoring data provided in the Home Credit Default Risk Kaggle competition hosted by the Home Credit Group. It provides an easy way to browse relevant data for each anonymized client, as well as their credit default risk score, a value predicted using a machine learning model created using the dataset.

The app is composed of two parts:
- A backend : a Flask server giving access to the data via an API. 

- A frontend : a Streamlit dashboard making calls to the backend to present relevant data.

The data modeling behind the creation of the machine learning model is detailed in the data_modeling submodule.

## Usage
### Without Docker
#### <u>API server</u>
To run the server, please execute the following from the Server directory:

```bash
pip install -r requirements.txt
python -m server
```


#### <u>Dashboard</u>
To run the dashboard, please execute the following from the Dashboard directory:

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

When run locally, the dashboard is accessible here:
```
http://localhost:8501
```


### With Docker
The API server and the Dashboard each have their own container that can be run separately, but the whole app is easily launched using Docker Compose.

To run the web app using Docker containers, please execute the following from the root directory:

```bash
docker-compose up
```
