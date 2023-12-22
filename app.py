from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .data.job import all_year_job, vehicle_job
from .etl import load, transform, extract
from .models import Base, Collision, Vehicle, Location, Date 
import pandas as pd
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://localhost/portfolio_db_test_1"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
with app.app_context():
    db.create_all()


all_year_data = pd.read_csv(f'{os.getcwd()}/data/SDOT_Collisions_All_Years.csv')
vehicle_data = pd.read_csv(f'{os.getcwd()}/data/SDOT_Collisions_Vehicles.csv')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/add')
def loading():

    trnsfrm_year_data = transform.Transform(all_year_data)
    d = trnsfrm_year_data.drop_duplicates()

    e = extract.Extract(all_year_job, d)
    data = e.get_required_data()

    load_db = load.Load([Collision, Location, Date], db, data)
    load_db.load_data()

    return {'data': 'Complete!'}






