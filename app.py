from flask import Flask, render_template, request
import numpy as np
import requests
import config
import pickle

# Load ML models
forest = pickle.load(open("models/yield_rf.pkl", "rb"))  # Yield prediction
cp = pickle.load(open("models/forest.pkl", "rb"))  # Crop price prediction
model = pickle.load(open("models/classifier.pkl", "rb"))
ferti = pickle.load(open("models/fertilizer.pkl", "rb"))
cr = pickle.load(open("models/RandomForest.pkl", "rb"))

app = Flask(__name__)


def weather_fetch(city_name):
    api_key = config.weather_api_key

    if not api_key:
        return None

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"appid": api_key, "q": city_name}

    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get("cod") != "404":
        main_data = data["main"]
        temperature = round(main_data["temp"] - 273.15, 2)
        humidity = main_data["humidity"]
        return temperature, humidity

    return None


@app.route("/")
def home():
    title = "Crop Harvest"
    return render_template("index.html", title=title)


@app.route("/crop-recommend")
def crop_recommend():
    title = "Crop Recommendation"
    return render_template("crop.html", title=title)


@app.route("/yeild")
def yeild():
    title = "Crop Yield Prediction"
    return render_template("crop_yeild.html", title=title)


@app.route("/crop_predict", methods=["POST"])
def crop_predict():
    title = "Crop Recommended"

    nitrogen = request.form["nitrogen"]
    phosphorous = request.form["phosphorous"]
    potassium = request.form["pottasium"]
    ph = request.form["ph"]
    rainfall = request.form["rainfall"]
    city = request.form["city"]

    weather_data = weather_fetch(city)

    if weather_data is not None:
        temperature, humidity = weather_data
        data = np.array(
            [[nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall]]
        )
        prediction = cr.predict(data)[0]

        return render_template(
            "crop-result.html", prediction=prediction, title=title
        )

    return render_template("try_again.html", title=title)


@app.route("/fer_predict", methods=["POST"])
def fer_predict():
    temp = request.form.get("temp")
    humi = request.form.get("humid")
    mois = request.form.get("mois")
    soil = request.form.get("soil")
    crop = request.form.get("crop")
    nitro = request.form.get("nitro")
    pota = request.form.get("pota")
    phosp = request.form.get("phos")

    input_data = [
        int(temp),
        int(humi),
        int(mois),
        int(soil),
        int(crop),
        int(nitro),
        int(pota),
        int(phosp),
    ]

    result = ferti.classes_[model.predict([input_data])]
    return render_template("fer_predict.html", res=result[0])


@app.route("/yeild-predict", methods=["POST"])
def yeild_predict():
    title = "Yield Predicted"

    state = request.form["stt"]
    district = request.form["city"]
    year = request.form["year"]
    season = request.form["season"]
    crop = request.form["crop"]
    temperature = request.form["Temperature"]
    humidity = request.form["humidity"]
    soil_moisture = request.form["soilmoisture"]
    area = request.form["area"]

    prediction = forest.predict(
        [
            [
                float(state),
                float(district),
                float(year),
                float(season),
                float(crop),
                float(temperature),
                float(humidity),
                float(soil_moisture),
                float(area),
            ]
        ]
    )

    predicted_yield = "{:.2f}".format(prediction[0])

    return render_template(
        "yeild_prediction.html", prediction=predicted_yield, title=title
    )


@app.route("/crop_price", methods=["GET", "POST"])
def crop_price():
    title = "Crop Price"
    return render_template("crop_price.html", title=title)


@app.route("/crop_fer", methods=["GET", "POST"])
def crop_fer():
    title = "Crop Fertilizer"
    return render_template("fer.html", title=title)


@app.route("/price_predict", methods=["POST"])
def price_predict():
    title = "Price Suggestion"

    state = int(request.form["stt"])
    district = int(request.form["city"])
    year = int(request.form["year"])
    season = int(request.form["season"])
    crop = int(request.form["crop"])

    price_result = cp.predict(
        [[float(state), float(district), float(year), float(season), float(crop)]]
    )

    return render_template(
        "price_prediction.html", title=title, p_result=price_result
    )


if __name__ == "__main__":
    app.run(debug=True)
