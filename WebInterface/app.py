"""
Sheth Riya Nimish
A0176880R
e0235287@u.nus.edu
Final Year Project

"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import json
import math
from pandas import DataFrame


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
model2= pickle.load(open('model2.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    print("hello")
    meandf= pd.read_csv("averages.csv")
    
    str_features = [str(x) for x in request.form.values()]
    
    int_features=[]
    for i in range (len(str_features)):
        if(str_features[i]=="NA" or str_features[i]==""):
            int_features.append(meandf.iloc[i][0])
        else:
            int_features.append(float(str_features[i]))
    
    
           
    final_features = [np.array(int_features)]
    print(final_features)
    prediction = model.predict(final_features)
    predictproba= model.predict_proba(final_features)
    

    predictionstext= ""
    if prediction ==1:
        predictiontext= 'The prediction for this material is magnetic and the probability of it being magnetic is {}'.format(predictproba[0][1])
        prediction2= model2.predict(final_features)
        predictproba2= model2.predict_proba(final_features)
        if prediction2==1:
            predictiontext= predictiontext+ ' and material is predicted to be ferromagnetic and the proability of it being ferromagnetic is {}'.format(predictproba2[0][1])
        else:
            predictiontext= predictiontext+ ' and material is predicted to be anti-ferromagnetic and the proability of it being anti-ferromagnetic is {}'.format(predictproba[0][0])
    else:
        predictiontext= 'The prediction for this material is non-magnetic and the probability of it being non-magnetic is {}'.format(predictproba[0][0])

    
    return render_template('index.html', prediction_text= predictiontext)
                         

if __name__ == "__main__":
    app.run(debug=True)
