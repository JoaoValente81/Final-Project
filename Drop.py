from flask import Flask, render_template, request

import requests
import pandas as pd
from apicall import get_temperature
from helper_function import run_model

import folium

from helper_function import createmap
import warnings

warnings.simplefilter('ignore')

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def dropdown():
    if request.method == 'POST':
        colours = ['Aveiro', 'Beja', 'Braga', 'Braganca', 'Castelo Branco', 'Coimbra', 'Evora', 'Faro', 'Guarda', 'Leiria', 'Lisboa', 'Porto', 'Setubal', 'Viana do Castelo', 'Portalegre', 'Santarém', 'Sines', 'Viseu', 'Vila Real']
        value = request.form.get('colour')
        
        Dict={'Aveiro':1010500, 'Beja':1020500, 'Braga':1030300, 'Braganca':1040200, 'Castelo Branco':1050200, 'Coimbra':1060300, 'Evora':1070500 , 'Faro':1080500, 'Guarda':1090700 , 'Leiria':1100900 , 'Lisboa':1110600, 'Porto':1131200, 'Setubal':1151200, 'Viana do Castelo':1160900, 'Portalegre':1121400, 'Santarém':1141600, 'Sines':1151300, 'Viseu':1182300 , 'Vila Real':1171400}
        citycode = str(Dict[value])
        temp=get_temperature(citycode)
        print(temp)
        pred =run_model(temp)

        return render_template('test.html', colours=colours, tables= [pred.to_html(classes='data')])
    else:
        colours = ['Aveiro', 'Beja', 'Braga', 'Braganca', 'Castelo Branco', 'Coimbra', 'Evora', 'Faro', 'Guarda', 'Leiria', 'Lisboa', 'Porto', 'Setubal', 'Viana do Castelo', 'Portalegre', 'Santarém', 'Sines']
        return render_template('test.html', colours=colours)



@app.route('/select', methods=['POST', 'GET'])
def select():
    if request.method == 'POST':
        value = request.form.get('colour')
        print(value)

@app.route('/view_map')
def index():
    folium_map = createmap()
  
    return folium_map._repr_html_()



@app.route('/pic', methods=['GET'])
def home():
    return render_template('post.html')

if __name__ == "__main__":
    app.run()