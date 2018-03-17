#################################################
#Dependencies
#################################################

import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import (Flask, render_template, jsonify, request, redirect)

import sqlite3
from flask import g


#################################################
# Database Setup
#################################################


engine = create_engine("sqlite:///gun_violence.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Gun_sales = Base.classes.gun_sales
Gun_law_grade = Base.classes.gun_law_grade
Mass_shootings = Base.classes.mass_shootings
State_laws_by_year = Base.classes.state_laws_by_year

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Page Routes

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/sources")
def sources():
    return render_template('sources.html')


# Data routes


# gun sales by type by state by year
@app.route("/gun_sales")
def gun_sales():
    results = session.query(Gun_sales.id, Gun_sales.year, Gun_sales.state, Gun_sales.handgun, Gun_sales.long_gun, Gun_sales.other).statement
    df_sales = pd.read_sql_query(results, session.bind)
    df_sales["new_id"] = df_sales["year"].astype(str) +df_sales["state"]
    del df_sales["id"]
    df_sales = df_sales[["new_id", "year", "state", "handgun", "long_gun", "other"]]
    sales_dict = {"gun_sales_id": df_sales["new_id"].values.tolist(),\
           "year": df_sales["year"].values.tolist(), \
           "state": df_sales["state"].values.tolist(),\
           "handgun": df_sales["handgun"].values.tolist(),\
           "long_gun": df_sales["long_gun"].values.tolist(),\
           "other": df_sales["other"].values.tolist()
          }
    return jsonify(sales_dict)

# list of states
@app.route("/states")
def states():
    results = session.query(Gun_sales.state).statement
    df_sales = pd.read_sql_query(results, session.bind)
    state_ids = []
    for num in range(56):
        state_ids.append(num)
    df_state_ids = pd.DataFrame(state_ids)
    df_state_ids = df_state_ids.iloc[1:56]
    df_state_ids = df_state_ids.reset_index(drop=True)
    df_state_ids = df_state_ids.rename(columns={0:"state_id"})
    state_names = df_sales["state"].iloc[0:55]
    df_states = pd.DataFrame(state_names)
    df_states["state_id"] = df_state_ids["state_id"]
    df_states = df_states[["state_id","state"]]
    states_dict = {"state_id": df_states["state_id"].values.tolist(),"state": df_states["state"].values.tolist()}
    return jsonify(states_dict)


if __name__ == "__main__":
    app.run(debug=True)