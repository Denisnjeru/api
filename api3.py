from flask import Flask, request, jsonify
#from sklearn.externals import joblib
import joblib 
from sklearn.preprocessing import LabelEncoder
import json
import pickle
import pandas as pd
from flask_restful import Resource, Api
import numpy as np


import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__)
api = Api(app)

# Load the model

MODEL = joblib.load('dtree_model.pkl')

MODEL_LABELS = ['SOUTH C', 'SOUTH B','ROYSAMBU', 'RONGAI', 
'PARKLANDS', 'KASARANI', 'KAHAWA WEST', 'NGARA']

@app.route('/hello')
def hello():
    return "Hello World!"



@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json(force=True)
    


    ID = data['email']
    pow_1 = data['placeOfWork']
    transport = data['meansOfTransport']
    living_space = data['houseSize']
    rent = data['rentAllocation']
    internet = data['internetAvailability']
    Garbage_collection = data['garbageCollection']
    Cable_TV = data['cableTV']
    family_size = data['familySize']
    monthly_budget = data['monthlyBudget']
    Water = data['waterAvailability']
    Electricity = data['electricityAvailability']
    Security = data['securityLevel']

    def pow_2():
        if pow_1 == 'CBD':
            pow_1 = 0
        elif pow_1 == 'Kasarani':
            pow_1 = 13
        elif pow_1 == 'Ngong':
            pow_1 = 31
        elif pow_1 == 'Roysambu':
            pow_1 = 37
        elif pow_1 == 'Karen':
            pow_1 = 12
        elif pow_1 == 'Wilson':
            pow_1 = 50
        elif pow_1 == 'Yaya centre':
            pow_1 =51
        elif pow_1 == 'Kilimani':
            pow_1 =17
        elif pow_1 == 'South b':
            pow_1 =42
        elif pow_1 == 'Mombasa Road':
            pow_1 =25
        elif pow_1 == 'Upperhill':
            pow_1 =47
        elif pow_1 == 'Ruiru':
            pow_1 =40
        elif pow_1 == 'Technical university of kenya':
            pow_1 =44
        elif pow_1 == None:
            pow_1 =32
        elif pow_1 == 'Rongai':
            pow_1 =36
        elif pow_1 == 'Ngong Road':
            pow_1 =30
        elif pow_1 == 'Parklands':
            pow_1 =55
        elif pow_1 == 'Town':
            pow_1 =45
        else:
            pred_class = 'ROYSAMBU'
    return place_of_work

    def living():
        #output the name of the predicted class
        if living_space == '1 Bedroom':
            living_space = 0
        elif living_space == 'Bedsitter':
            living_space = 4
        elif living_space == '2 Bedroom':
            living_space = 1
        elif living_space == '3 Bedroom':
            living_space = 2
    return living_space

    def trans():
        #output the name of the predicted class
        if transport == 'Matatu':
            transport = 1
        elif transport == 'Bicycle':
            transport = 0
        elif transport == 'Private':
            transport = 3
        elif transport == 'Public':
            transport = 4
    return transport

    def monthlybudget():
        #output the name of the predicted class
        if monthly_budget== '15000-30000':
            monthly_budget = 0
        elif monthly_budget == 'more 100+':
            monthly_budget= 6
        elif monthly_budget == '30,000-50000':
            monthly_budget = 1
        elif monthly_budget == '5000-15000':
            monthly_budget = 3
        elif monthly_budget == 'less 5000':
            monthly_budget = 5
        elif monthly_budget == '50000':
            monthly_budget = 4
    return monthly_budget

    def rental():
        #output the name of the predicted class
        if rent== '10000-20000':
            rent = 0
        elif rent == '5000-10000':
            rent= 2
        elif rent == '30000-40000':
            rent = 4
        elif rent == '20000-30000':
            rent = 3
        elif rent == '40+':
            rent = 5
        #elif rent == '0-5000':
            #rent = 0
    return rent

    # data preprocessing
    # Label Encoding the categorical columns



    # Our model expects a list of records
    features = [[pow_1, transport, living_space, rent, monthly_budget]]

    


    # Use the model to predict the class
    api_prediction = pd.DataFrame(MODEL.predict_proba(features), columns=([1, 2, 3, 4, 5, 6, 7, 8]))
    

    api_prediction = api_prediction.sort_values(by=0, axis=1, ascending=False)
    #slice to get the first 4 columns
    api_prediction = api_prediction.iloc[:,0:3]
    api_prediction = api_prediction.columns
    
    
    #predicting the probability of the class
    # pred_proba = MODEL.predict_proba(features)
    
    #output the name of the predicted class
    if api_prediction == 1:
        pred_class = 'NGARA'
    elif api_prediction == 2:
        pred_class = 'RONGAI'
    elif api_prediction == 3:
        pred_class = 'KASARANI'
    elif api_prediction == 4:
        pred_class = 'SOUTH C'
    elif api_prediction == 5:
        pred_class = 'SOUTH B'
    elif api_prediction == 6:
        pred_class = 'KAHAWA WEST'
    elif api_prediction == 7:
        pred_class = 'PARKLANDS'
    else:
        pred_class = 'ROYSAMBU'
    
    
    # Create and send a response to the API caller
    return jsonify(ID=ID, prediction=pred_class)



if __name__ == '__main__':
    app.run(port=5000, debug=True)
