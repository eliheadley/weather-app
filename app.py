import requests
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
base_url = "https://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)

@app.route("/")
def index():   
    return render_template('index.html')


@app.route("/get-weather", methods=["POST", "GET"])
def get_weather():
    weather = None
    city = request.args.get('city')
    if city:
        complete_url = f"{base_url}?q={city}&appid={api_key}&units=imperial"
        response = requests.get(complete_url)
        print(response.status_code)
        if response.status_code == 200:
            weather = response.json()
        else:
            weather = {'error': f"Could not fetch the weather for for '{city}'."}
        
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run()