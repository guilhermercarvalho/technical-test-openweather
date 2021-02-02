from flask_marshmallow import Marshmallow
from .model import Weather

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class WeatherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Weather
        load_instance = True
