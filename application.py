from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            fly_ash=float(request.form.get('fly_ash')),
            average_aggregate=float(request.form.get('average_aggregate')),
            cement_water_ratio=float(request.form.get('cement_water_ratio')),
            blast_furnace_slag=float(request.form.get('blast_furnace_slag')),
            super_plasticizer=float(request.form.get('super_plasticizer')),
            age=int(request.form.get('age'))
        )
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Pass results to template
        return render_template('home.html', prediction= f"Predicted Concrete Strength is {results[0]} /MPa", image='https://expertcivil.com/wp-content/uploads/2021/05/Concrete-Mixer-750x570.jpg')   

if __name__=="__main__":
    app.run(host="0.0.0.0")        

