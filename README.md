
# insurance-premium-prediction-fastapi
A FastAPI based API for the insurance premium prediction ML project

# Insurance Premium Prediction API (FastAPI)

A FastAPI-based API for predicting insurance premiums using a trained machine learning model.  

## Project Overview

This project provides a REST API built with FastAPI that allows users to input customer data and receive a predicted insurance premium. It uses a pre-trained ML model (saved as `model.pkl`) under the hood, making it easy to integrate into applications or services that require premium estimation.  

**Why this project matters:**  
- Automates insurance premium estimation.  
- Offers a simple HTTP API — easy to integrate.  
- Demonstrates end-to-end ML + API deployment with minimal effort.  

## Features

- Predict insurance premium based on user input data (e.g. age, smoking status, number of children, etc.).  
- Exposes endpoints for JSON input and output.  
- Sample input/output via simple Python script or front-end.  
- Ready-to-use model file (`model.pkl`) — no training required.  
- Easy to extend: you can retrain the model, update features, or wrap into a larger service.  

## 📁 Project Structure
.
├── app.py # FastAPI application entry point

├── predict.py # Prediction logic (load model, preprocess input, return premium)

├── user_input.py # Helper for user input (optional)

├── requirement.txt # Project dependencies

├── model.pkl # Pre-trained ML model for prediction

├── insurance.csv # (Optional) dataset used originally for training

├── fastapi_ml_model.ipynb # Jupyter notebook with training / model building code

└── README.md # Project documentation (this file)


## Installation & Setup

### Prerequisites

- Python 3.7 or newer  
- `pip` installed  

### Installation

```bash
# Clone the repository
git clone https://github.com/ankit8445singh/insurance-premium-prediction-fastapi.git
cd insurance-premium-prediction-fastapi

# Install dependencies
pip install -r requirement.txt


Running the API locally
uvicorn app:app --reload


After this, the API will be available at http://127.0.0.1:8000/.



## Running the API locally
uvicorn app:app --reload

After this, the API will be available at http://127.0.0.1:8000/.



##Usage Example

##Example using curl:

curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "age": 29,
           "sex": "male",
           "bmi": 26.2,
           "children": 2,
           "smoker": "no",
           "region": "southeast"
         }'

