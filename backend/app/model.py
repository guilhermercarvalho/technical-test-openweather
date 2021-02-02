from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dt = db.Column(db.DateTime, default=datetime.utcnow)
    city = db.Column(db.String(255))
    country = db.Column(db.String(2))
    temp = db.Column(db.Float)
    temp_min = db.Column(db.Float)
    temp_max = db.Column(db.Float)
    feels_like = db.Column(db.Float)
    weather_main = db.Column(db.String(255))
    weather_description = db.Column(db.String(255))
    weather_icon = db.Column(db.String(3))
    pressure = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    visibility = db.Column(db.Integer)
    wind_speed = db.Column(db.Float)
    cloudiness = db.Column(db.Integer)