# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:33:49 2023

@author: Jeyaram
"""

from flask import Flask,render_template,request
app = Flask(__name__)

import pickle
model = pickle.load(open('model.pkl','rb'))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home_walmart.html')

@app.route('/walmart')
def walmart():
    return render_template('walmart_home_page.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/login',methods=['POST'])
def login():
    st = request.form["storeId"]
    
    dt = request.form["date"]
    
    temp = request.form["Temperature"]
    
    fp = request.form["fuelP"]
    cpi = request.form["cpi"]
    pur= request.form["unemployment"] 
    dates = ['01-01-2023','16-01-2023','20-02-2023','29-05-2023','04-07-2023','04-09-2023','09-10-2023','10-11-2023','23-11-2023','25-12-2023']
    if dt in dates:
        holiday = 1
    else:
        holiday = 0
    t = [[float(st),float(holiday),float(temp),float(fp),float(cpi),float(pur)]]
    print(t)
    t  =scaler.transform(t)
    print(t)
    output = model.predict(t)
    output = round(output[0])
    output = ('{:,}'.format(output))
    print(output)
    
    return render_template("walmart_home_page.html", y ="The predicted sales for the week is " + str(output))

if __name__=="__main__":
    app.run(debug=False)


    
