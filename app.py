from flask import Flask,request,app,render_template
import pickle
import numpy as np
import pandas as pd 
from pymongo import MongoClient
app=Flask(__name__)
model=pickle.load(open(r'C:\Users\PC\Desktop\Linear Regression\regression.pkl','rb'))
@app.route('/')
def index():
     return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
     result=""
     if request.method=='POST':
          Year=float(request.form.get('Year'))
          Experience=float(request.form.get('Experience'))
          result=model.predict([[Year,Experience]])[0]
          return render_template('index.html',result=result)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

