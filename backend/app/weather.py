from logging import error
from flask import Blueprint, current_app, request, jsonify
from requests import get
from dotenv import load_dotenv
from os import getenv
from .model import Weather
from .serealizer import WeatherSchema

load_dotenv()

OWM_BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"
OWM_LANG = "pt_br"
OWM_UNITS = "metric"
OWM_KEY = getenv("OWM_KEY")

params = {
    "lang": OWM_LANG,
    "units": OWM_UNITS,
    "appid": OWM_KEY
}

bp_weather = Blueprint('weather', __name__)


@bp_weather.route('/history', methods=['GET'])
def history():
    ws = WeatherSchema(many=True)
    result = Weather.query.all()
    return ws.jsonify(result), 200


@bp_weather.route('/add', methods=['POST'])
def add():
    content = request.get_json()
    data = get_weather(content.get('city', None))

    if data.get("error", False):
        return jsonify({"message": data["msg"]}), data["error"]

    ws = WeatherSchema()
    weather = ws.load(data)
    current_app.db.session.add(weather)
    current_app.db.session.commit()
    return ws.jsonify(weather), 201


def get_weather(city):
    global params
    params.update({"q": city})

    res = get(
        url=OWM_BASE_URL,
        params=params
    )

    if not res.ok:
        return {
            "error": res.status_code,
            "msg": res.json()["message"]
        }

    res = res.json()


    return {
        "city": res["city"]["name"],
        "country": res["city"]["country"],
        "temp": res["list"][0]["main"]["temp"],
        "temp_min": res["list"][0]["main"]["temp_min"],
        "temp_max": res["list"][0]["main"]["temp_max"],
        "feels_like": res["list"][0]["main"]["feels_like"],
        "weather_main": res["list"][0]["weather"][0]["main"],
        "weather_description": res["list"][0]["weather"][0]["description"],
        "weather_icon": res["list"][0]["weather"][0]["icon"],
        "pressure": res["list"][0]["main"]["pressure"],
        "humidity": res["list"][0]["main"]["humidity"],
        "visibility": res["list"][0]["visibility"],
        "wind_speed": res["list"][0]["wind"]["speed"],
        "cloudiness": res["list"][0]["clouds"]["all"]
    }


@bp_weather.route('/delete/<id>', methods=['GET'])
def delete(id):
    Weather.query.filter(Weather.id == id).delete()
    current_app.db.session.commit()
    return jsonify("Deleted"), 202
