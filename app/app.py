from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='static/none.png', href3='')
    else:
        myage = request.form['age']
        mysalary = request.form['salary']
        mygender = request.form['gender']

        mypredict = ''
        if str(myage) =='' or  str(mysalary)=='':
            return render_template('index.html', href2='static/none.png', href3='Please insert your age and salary range.')
        else:
            model = load('app/occupation-recommender.joblib')
            np_arr = np.array([myage, mygender, mysalary])
            predictions = model.predict([np_arr])  
            predictions_to_str = str(predictions)
            
            if 'cashier' in predictions_to_str:
                if mygender == 1:
                    mypredict = 'static/female-cashier.jpg'
                else:
                    mypredict = 'static/male-cashier.jpg'    
            elif 'doctor' in predictions_to_str:
                if mygender == 1:
                    mypredict = 'static/female-docter.jpg'
                else:
                    mypredict = 'static/male-doctor.jpg'
            elif 'engineer' in predictions_to_str:
                if mygender == 1:
                    mypredict = 'static/female-cashier.jpg'
                else:
                    mypredict = 'static/male-engineer.jpg'
            elif 'plumber' in predictions_to_str:
                if mygender == 1:
                    mypredict = 'static/female-plumber.jpg'
                    else:
                        mypredict = 'static/male-plumber.jpg'
            elif 'whole wheat' in predictions_to_str:
                mypredict = 'static/whole-wheat-bread.jpg' 
            else:
                mypredict = 'static/none.png' 
                
            return render_template('index.html', href2=str(mypredict), href3='This is the recommendation!'+predictions_to_str)
        

