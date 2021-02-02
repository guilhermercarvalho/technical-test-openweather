from flask import Flask, render_template, url_for
from flask_migrate import Migrate
from flask_cors import CORS
from .model import configure as config_db
from .serealizer import configure as config_ma

def create_app():
    app = Flask("__name__")
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@db:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    config_db(app)
    config_ma(app)
    
    Migrate(app, app.db)

    from .weather import bp_weather
    app.register_blueprint(bp_weather)

    return app