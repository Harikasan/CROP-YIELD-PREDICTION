# Crop Yield Prediction

## Overview

Crop Yield Prediction is a machine learning-powered web application designed to assist farmers, agricultural researchers, and planners in making data-driven decisions. The application leverages multiple machine learning models to provide crop recommendations, crop yield predictions, fertilizer suggestions, and crop price estimations based on environmental, soil, and agricultural parameters.

### Key Features

* Crop Recommendation System
* Crop Yield Prediction
* Fertilizer Recommendation
* Crop Price Prediction
* Weather Data Integration using OpenWeather API
* User-Friendly Flask Web Interface

---

## Technology Stack

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* NumPy
* Pandas

### Deployment

* Gunicorn
* Render

### Data Sources

* OpenWeather API
* Agricultural Datasets
* IoT Sensor Data (ThingSpeak Integration)

---

## Project Structure

```text
CROP-YIELD-PREDICTION/
│
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── models/
│   ├── yield_rf.pkl
│   ├── forest.pkl
│   ├── classifier.pkl
│   ├── fertilizer.pkl
│   └── RandomForest.pkl
│
├── templates/
├── static/
│
├── notebooks/
│
└── README.md
```

---

## Clone the Repository

```bash
git clone https://github.com/Harikasan/CROP-YIELD-PREDICTION.git
cd CROP-YIELD-PREDICTION
```

---

## Download Model Files

This project uses Git LFS to store trained machine learning models.

After cloning the repository, run:

### macOS

```bash
brew install git-lfs
git lfs install
git lfs pull
```

### Windows

Install Git LFS from https://git-lfs.com

Then run:

```bash
git lfs install
git lfs pull
```

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

This project uses OpenWeather API to retrieve weather information required for crop recommendations.

### Windows

```bash
set WEATHER_API_KEY=your_openweather_api_key
```

### macOS / Linux

```bash
export WEATHER_API_KEY=your_openweather_api_key
```

### config.py

```python
import os

weather_api_key = os.getenv("WEATHER_API_KEY")
```

> Never commit API keys, credentials, or secrets to GitHub.

---

## Run the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## Application Modules

### Crop Recommendation

Predicts the most suitable crop based on:

* Nitrogen (N)
* Phosphorous (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall

### Crop Yield Prediction

Predicts expected crop yield using:

* State
* District
* Crop Type
* Season
* Temperature
* Humidity
* Soil Moisture
* Cultivation Area

### Fertilizer Recommendation

Recommends suitable fertilizer based on:

* Soil Type
* Crop Type
* Nitrogen Content
* Phosphorous Content
* Potassium Content
* Moisture
* Temperature
* Humidity

### Crop Price Prediction

Estimates crop market prices using historical agricultural production and market data.

---

## Machine Learning Models

| Model File       | Purpose                   |
| ---------------- | ------------------------- |
| yield_rf.pkl     | Crop Yield Prediction     |
| RandomForest.pkl | Crop Recommendation       |
| classifier.pkl   | Fertilizer Classification |
| fertilizer.pkl   | Fertilizer Label Mapping  |
| forest.pkl       | Crop Price Prediction     |

---



## Troubleshooting

### Model Loading Errors

Verify that all model files are present inside the `models/` directory.

### Weather API Errors

Verify:

* OpenWeather API key is valid
* Environment variable is configured correctly

### Dependency Errors

Reinstall packages:

```bash
pip install -r requirements.txt
```

### Deployment Failures

Check:

* requirements.txt
* Environment Variables
* Gunicorn Start Command
* Model File Paths

---

## Future Enhancements

* Docker Containerization
* CI/CD Pipeline using GitHub Actions
* REST API Endpoints
* Advanced Weather Forecast Integration
* Improved Model Accuracy
* Cloud Database Integration
* Mobile Responsive Interface

---

## Author

**Harika Attipatla**

Master's in Computer Science
University of Texas at Arlington

GitHub: https://github.com/Harikasan
