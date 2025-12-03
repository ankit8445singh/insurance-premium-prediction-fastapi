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

