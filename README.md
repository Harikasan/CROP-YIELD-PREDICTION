# CROP-YIELD-PREDICTION
A machine learning–powered web application that predicts crop yield based on environmental and soil parameters such as rainfall, temperature, humidity, and NPK levels. Built with a Flask backend to deliver real-time predictions through an interactive web interface.  Tech: Python, Flask, Scikit-learn, Pandas, NumPy.

## Features

- Crop yield prediction
- Crop recommendation based on NPK, pH, rainfall, temperature, and humidity
- Fertilizer recommendation
- Crop price prediction
- Weather-based input support using OpenWeather API
- Flask web interface with HTML templates

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Pickle
- HTML/CSS
- Gunicorn

## Project Structure

```bash
CROP-YIELD-PREDICTION/
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── models/
│   ├── yield_rf.pkl
│   ├── forest.pkl
│   ├── classifier.pkl
│   ├── fertilizer.pkl
│   └── RandomForest.pkl
├── templates/
├── static/
└── notebooks/
