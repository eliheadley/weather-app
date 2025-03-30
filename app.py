import requests
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

def test():
    print(os.getenv("OPENWEATHER_API_KEY"))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run()