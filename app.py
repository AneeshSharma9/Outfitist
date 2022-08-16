import requests, json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        api_key = "2b540f45bc7ca92b95eb259f5ddd9e46"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = text
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            return (" Temperature (in kelvin unit) = " +
                            str(current_temperature) +
                "\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                "\n humidity (in percentage) = " +
                            str(current_humidity) +
                "\n description = " +
                            str(weather_description))
        else:
            return (" City Not Found ")
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")


    