from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

with open('stroke-model.bin', 'rb') as f_in:
    model = pickle.load(f_in)

def single_patient_prediction(patient, model):
    y_pred = model.predict(patient)
    y_pred_prob = model.predict_proba(patient)[:, 1]
    y_pred_prob = y_pred_prob * 100
    return y_pred, y_pred_prob[0]

app = Flask('Stroke-Prediction')

@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()
    patient = pd.read_json(patient, orient='columns')
 
    stroke, probs = single_patient_prediction(patient, model)
   
    result = {        
        'stroke_perc_probability': float(probs), 
        'likely_to_suffer_stroke': bool(stroke),                
    }                                  
 
    return jsonify(result)  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9800)