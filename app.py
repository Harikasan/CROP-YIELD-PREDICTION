
from flask import Flask, render_template, request
from markupsafe import Markup
import numpy as np
import pandas as pd

import requests
import config
import pickle
import io

from PIL import Image

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load ML model
forest = pickle.load(open('models/yield_rf.pkl', 'rb'))  # yield
cp = pickle.load(open('models/forest.pkl', 'rb'))  # price

model = pickle.load(open('models/classifier.pkl','rb'))
ferti = pickle.load(open('models/fertilizer.pkl','rb'))
cr = pickle.load(open('models/RandomForest.pkl', 'rb'))


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = config.weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    print('vgj,hDS|m n')
    print(response)

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None





app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Crop harvest'
    return render_template('index.html', title=title)

# render crop recommendation form page


@ app.route('/crop-recommend')
def crop_recommend():
    import requests
    import pandas as pd
    data=requests.get("https://api.thingspeak.com/channels/2042463/feeds.json?api_key=Y3CYVNTXSR99OSVE&results=2")
    p=data.json()['feeds'][-1]['field3']
    n=data.json()['feeds'][-1]['field4']
    k=data.json()['feeds'][-1]['field5']
    temp=data.json()['feeds'][-1]['field2']
    title = 'Crop Recommendation'
    # , n=n, p=p, k=k, temp=temp)
    return render_template('crop.html', title=title) #,n=n)

# render fertilizer recommendation form page


@ app.route('/yeild')
def yeild():
    import requests
    import pandas as pd
    data=requests.get("https://api.thingspeak.com/channels/2042463/feeds.json?api_key=Y3CYVNTXSR99OSVE&results=2")
    temp=data.json()['feeds'][-1]['field3']
    hum=data.json()['feeds'][-1]['field1']
    moi=data.json()['feeds'][-1]['field2']
    title = 'crop yeild prediction'

    # , temp=temp, hum=hum)
    return render_template('crop_yeild.html', title=title ) #,temp=temp,hum=hum,moi=moi)



# render crop recommendation result page


@ app.route('/crop_predict', methods=['POST'])
def crop_predict():
    title = 'Crop Recommended'

    if request.method == 'POST':
        N = request.form['nitrogen']
        P = request.form['phosphorous']
        K = request.form['pottasium']
        ph = request.form['ph']
        rainfall = request.form['rainfall']
        state = request.form['stt']
        city = request.form['city']

        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = cr.predict(data)
            final_prediction = my_prediction[0]

            return render_template('crop-result.html', prediction=final_prediction, title=title)
        else:
            return render_template('try_again.html', title=title)
# render fertilizer recommendation result page

@app.route('/fer_predict',methods=['POST'])
def fer_predict():
    temp = request.form.get('temp')
    humi = request.form.get('humid')
    mois = request.form.get('mois')
    soil = request.form.get('soil')
    crop = request.form.get('crop')
    nitro = request.form.get('nitro')
    pota = request.form.get('pota')
    phosp = request.form.get('phos')
    input = [int(temp),int(humi),int(mois),int(soil),int(crop),int(nitro),int(pota),int(phosp)]

    res = ferti.classes_[model.predict([input])]

    return render_template('fer_predict.html',res = res[0])
@ app.route('/yeild-predict', methods=['POST'])
def yeild_predict():
    title = 'yeild predicted'

    if request.method == 'POST':
        state = request.form['stt']
        district = request.form['city']
        year = request.form['year']
        season = request.form['season']
        crop = request.form['crop']
        Temperature = request.form['Temperature']
        humidity = request.form['humidity']
        soilmoisture = request.form['soilmoisture']
        area = request.form['area']

        out_1 = forest.predict([[float(state),
                                 float(district),
                                 float(year),
                                 float(season),
                                 float(crop),
                                 float(Temperature),
                                 float(humidity),
                                 float(soilmoisture),
                                 float(area)]])
        print("the yield is --->   {}    tons".format(out_1[0]))
        out_yield="{:.2f}".format(out_1[0])
##        N = int(request.form['nitrogen'])
##        P = int(request.form['phosphorous'])
##        K = int(request.form['pottasium'])
##        ph = float(request.form['ph'])
##        rainfall = float(request.form['rainfall'])
##
# state = request.form.get("stt")
##        city = request.form.get("city")
##
# if weather_fetch(city) != None:
##            temperature, humidity = weather_fetch(city)
##            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
##            my_prediction = crop_recommendation_model.predict(data)
##            final_prediction = my_prediction[0]

        return render_template('yeild_prediction.html', prediction=out_yield, title=title)

    return render_template('try_again.html', title=title)


# render disease prediction result page


@app.route('/crop_price', methods=['GET', 'POST'])
def crop_price():
    # return "this is crop prediction page"
    title = 'crop price'
    return render_template('crop_price.html', title=title)

@app.route('/crop_fer', methods=['GET', 'POST'])
def crop_fer():
    import requests
    import pandas as pd
    data=requests.get("https://api.thingspeak.com/channels/2042463/feeds.json?api_key=Y3CYVNTXSR99OSVE&results=2")
    p=data.json()['feeds'][-1]['field3']
    n=data.json()['feeds'][-1]['field4']
    k=data.json()['feeds'][-1]['field5']
    temp=data.json()['feeds'][-1]['field2']
    # return "this is crop prediction page"
    title = 'crop Fertilizer'
    return render_template('fer.html', title=title) #,n=n)


@ app.route('/price_predict', methods=['POST'])
def price_predict():
    title = 'price Suggestion'
    if request.method == 'POST':
        state = int(request.form['stt'])
        district = int(request.form['city'])
        year = int(request.form['year'])
        season = int(request.form['season'])
        crop = int(request.form['crop'])

        p_result = cp.predict([[float(state),
                                float(district),
                                float(year),
                                float(season),
                                float(crop)]])

        return render_template('price_prediction.html', title=title, p_result=p_result)
    return render_template('try_again.html', title=title)


# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
