import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("notebook","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self,
                 fly_ash: float,
                 average_aggregate: float,
                 cement_water_ratio: float,
                 blast_furnace_slag: float,
                 super_plasticizer: float,
                 age: int):
        self.fly_ash = fly_ash
        self.average_aggregate = average_aggregate
        self.cement_water_ratio = cement_water_ratio
        self.blast_furnace_slag = blast_furnace_slag
        self.super_plasticizer = super_plasticizer
        self.age = age

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Fly Ash": [self.fly_ash],
                "average_aggregate": [self.average_aggregate],
                "cement_water_ratio": [self.cement_water_ratio],
                "Blast Furnace Slag": [self.blast_furnace_slag],
                "Superplasticizer": [self.super_plasticizer],
                "Age": [self.age],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            # If features is a single instance of CustomData, convert it to a DataFrame
            if isinstance(features, CustomData):
                features = features.get_data_as_data_frame()

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)
