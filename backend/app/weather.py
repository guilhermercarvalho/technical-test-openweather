from logging import error
from flask import Blueprint, current_app, request, jsonify
from requests import get
from dotenv import load_dotenv
from os import getenv
from .model import Weather
from .serealizer import WeatherSchema

load_dotenv()

OWM_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
OWM_LANG = "pt_br"
OWM_UNITS = "metric"
OWM_KEY = getenv("OWM_KEY")

params = {
    "lang": OWM_LANG,
    "metrics": OWM_UNITS,
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
        "city": res["name"],
        "country": res["sys"]["country"],
        "temp": res["main"]["temp"],
        "temp_min": res["main"]["temp_min"],
        "temp_max": res["main"]["temp_max"],
        "feels_like": res["main"]["feels_like"],
        "weather_main": res["weather"][0]["main"],
        "weather_description": res["weather"][0]["description"],
        "weather_icon": res["weather"][0]["icon"],
        "pressure": res["main"]["pressure"],
        "humidity": res["main"]["humidity"],
        "visibility": res["visibility"],
        "wind_speed": res["wind"]["speed"],
        "cloudiness": res["clouds"]["all"]
    }


@bp_weather.route('/delete/<id>', methods=['GET'])
def delete(id):
    Weather.query.filter(Weather.id == id).delete()
    current_app.db.session.commit()
    return jsonify("Deleted"), 202
