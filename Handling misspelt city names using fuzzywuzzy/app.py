from flask import Flask, render_template,request
from fuzzywuzzy import process
from connect_db import db_connect
import pandas as pd
app=Flask(__name__)  #creating an instance of Flask class for our web app

@app.route('/')
def first_page():
    return render_template('index.html')

def similar_res_finder(subject, universe, limit):
    results = process.extract(subject, universe, limit=limit)
    print(results)
    return str(results)

@app.route('/',methods=['POST'])
def show_results():
    if request.method == 'POST':
        city_name = request.form.get('city')
        print(city_name)
        cities = db_connect('****@123','project_flask1','localhost','root')
        result = similar_res_finder(city_name, list(cities['city']),3)
        return result

if __name__ == '__main__':
    app.run()